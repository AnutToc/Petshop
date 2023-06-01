from django.contrib import admin
from django.urls import path
from myapp import views
from django.urls import include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="home"),
    path("main/", views.main, name="main"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('main/', views.main, name='main'),
    path('cart/', include(('cart1.urls', 'cart'), namespace='cart')),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
