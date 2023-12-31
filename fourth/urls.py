from django.urls import path, re_path
from . views import *

urlpatterns =[
    path('', ManHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='addpage'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
    ]