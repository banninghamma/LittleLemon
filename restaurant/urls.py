#define URL route for index() view
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='get_menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='get_single_menu_item'),
    path('api-token-auth/', obtain_auth_token),
]