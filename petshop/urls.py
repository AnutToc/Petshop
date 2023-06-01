from django.contrib import admin
from django.urls import path
from myapp import views
from cart1.views import add_to_cart
from django.urls import include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'myapp'

urlpatterns = [
    path("", views.petshop, name="home"),
    path("main/", views.main, name="main"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('main/', views.main, name='main'),
    path('cart/', include(('cart1.urls', 'cart'), namespace='cart')),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    
    path("petshop/", views.petshop, name="index1"),
    path("petshop/about", views.petshop_about, name="about"),
    path("petshop/blog", views.petshop_blog, name="blog"),
    path("petshop/contact", views.petshop_contact, name="contact"),
    path("petshop/detail", views.petshop_detail, name="detail"),
    
    path("purr/about", views.purr_about, name="about"),
    path("purr/contact", views.purr_contact, name="contact"),
    path("purr/gallery", views.purr_gallery, name="gallery"),
    path("purr/", views.purr_index, name="index"),
    
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
