from django.urls import path

from .views import *

urlpatterns = [
	path('', index, name='home'),
	path('shop/', shop, name='shop'),
	path('shop/<int:pk>/', special, name='special'),
	path('shop/product-<int:pk>/', detail_of_good, name='detail_of_good'),
	path('account/', account, name='account'),
	path('logout/', logoutPage, name='logout'),
	path('login/', loginPage, name='login'),
	path('register/', registerPage, name='register'),
]

