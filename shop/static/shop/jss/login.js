// Открывает модальное окно при нажатии на кнопку "Log in"
document.getElementById("loginBtn").addEventListener("click", function() {
    var modalId = this.getAttribute("data-modal-target");
    var modal = document.querySelector(modalId);
    modal.style.display = "block";
});

// Закрывает модальное окно при нажатии на крестик
document.querySelector(".close").addEventListener("click", function() {
    var modal = this.closest(".modal");
    modal.style.display = "none";
});

// Обработка отправки формы
document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Предотвращение отправки формы по умолчанию

    var form = this;
    var formData = new FormData(form);

    fetch(form.action, {
        method: form.method,
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = "/"; // Перенаправление на главную страницу после успешного входа
        } else {
            // Обработка ошибок, если не удалось войти
            console.log(data.errors);
        }
    })
    .catch(error => {
        console.log(error);
    });
});


// Получение кнопок "Добавить в корзину"
var addToCartButtons = document.getElementsByClassName('add-to-cart');

// Получение списка для отображения товаров в корзине
var cartItems = document.getElementsByClassName('cart-items')[0];

// Обработка нажатия на кнопку "Добавить в корзину"
for (var i = 0; i < addToCartButtons.length; i++) {
  var button = addToCartButtons[i];
  button.addEventListener('click', addToCartClicked);
}

// Функция обработки нажатия на кнопку "Добавить в корзину"
function addToCartClicked(event) {
  var button = event.target;
  var product = button.parentElement;
  var title = product.getElementsByTagName('h2')[0].innerText;
  var price = product.getElementsByTagName('p')[0].innerText;
  var imageSrc = product.getElementsByTagName('img')[0].src;

  addItemToCart(title, price, imageSrc);
  updateCartTotal();
}

// Функция добавления товара в корзину
function addItemToCart(title, price, imageSrc) {
  var cartRow = document.createElement('li');
  cartRow.classList.add('cart-row');
  var cartRowContents = `
    <img src="${imageSrc}" alt="${title}" class="cart-item-image">
    <div class="cart-item">
      <span class="cart-item-title">${title}</span>
      <span class="cart-item-price">${price}</span>
      <button class="cart-item-remove">Удалить</button>
    </div>`;
  cartRow.innerHTML = cartRowContents;
  cartItems.appendChild(cartRow);

  // Обработка нажатия на кнопку "Удалить"
  var removeButtons = cartRow.getElementsByClassName('cart-item-remove');
  for (var i = 0; i < removeButtons.length; i++) {
    var button = removeButtons[i];
    button.addEventListener('click', removeCartItem);
  }
}

// Функция удаления товара из корзины
function removeCartItem(event) {
  var buttonClicked = event.target;
  buttonClicked.parentElement.parentElement.remove();
  updateCartTotal();
}

// Функция обновления общей суммы в корзине
function updateCartTotal() {
  var cartRows = cartItems.getElementsByClassName('cart-row');
  var total = 0;
  for (var i = 0; i < cartRows.length; i++) {
    var cartRow = cartRows[i];
    var priceElement = cartRow.getElementsByClassName('cart-item-price')[0];
    var price = parseFloat(priceElement.innerText.replace('руб.', ''));
    total += price;
  }
  var cartTotal = document.getElementsByClassName('cart-total')[0];
  cartTotal.innerText = total.toFixed(2) + ' руб.';
}
