from django.urls import path

from . import views
from .views import show_category

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:post_id>', views.show_post, name='post'),
    path('category/<int:cat_id>', views.show_category, name='category'),
    path('registration/', views.registration_view, name='registration'),
    path('user_cabinet/', views.user_cabinet, name='user_cabinet'),
]
