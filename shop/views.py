from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
# from cart.forms import CartAddProductForm
from sport_shop.forms import RegistrationForm
from .models import *

menu = [{'title': 'About sport shop', 'url_name': 'about'},
        {'title': 'Contact with us', 'url_name': 'contact'},
        {'title': 'Log in', 'url_name': 'login'},
        {'title': 'Registration', 'url_name': 'registration'},
        {'title': 'User Cabinet', 'url_name': 'user_cabinet'}
        ]


def index(requests):
    posts = Product.objects.all()
    cats = Category.objects.all()
    context = {'menu': menu,
               'cats': cats,
               'title': 'Homepage',
               'posts': posts,
               'cat_selected': 0}
    return render(requests, 'shop/index.html', context=context)


def about(requests):
    posts = Product.objects.all()
    return render(requests, 'shop/about.html', {'menu': menu,
                                                'title': 'About sport shop',
                                                'posts': posts})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return JsonResponse({'success': False, 'errors': 'Invalid username or password'})
    else:
        return render(request, 'shop/login.html')


def show_post(requests, post_id):
    post = get_object_or_404(Product, pk=post_id)
    context = {'menu': menu,
               'post': post,
               'name': post.name,
               'cat_selected': post.cat_id,
               }
    return render(requests, 'shop/post.html', context=context)


def show_category(requests, cat_id):
    posts = Product.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    context = {'menu': menu,
               'cats': cats,
               'posts': posts,
               'cat_selected': cat_id}
    return render(requests, 'shop/index.html', context)


def pageNotFound(requests, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def contact(requests):
    posts = Product.objects.all()
    return render(requests, 'shop/contact.html', {'menu': menu,
                                                  'title': 'About sport shop',
                                                  'posts': posts})


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered.')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'shop/registration.html', {'form': form})


@login_required
def user_cabinet(request):
    return render(request, 'shop/user_cabinet.html')

# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'shop/product/detail.html', {'product': product,
#                                                         'cart_product_form': cart_product_form})