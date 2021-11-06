from django.urls import path

from store.settings import MEDIA_ROOT, MEDIA_URL
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('register/user',views.registeruser,name="registeruser"),
    path('login/user',views.handlelogin,name="loginuser"),
    path('logout',views.handlelogout,name="logout"),
    path('addtocart',views.AddToCart,name='addtocart'),
    path('checkout',views.Checkout,name='checkout')
   
]+  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)