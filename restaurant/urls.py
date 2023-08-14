#define URL route for index() view
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_item'),
    path('reservations/', views.reservations, name="reservations"),
    path('bookings', views.bookings, name='bookings'), 
    path('api-token-auth/', obtain_auth_token),
]