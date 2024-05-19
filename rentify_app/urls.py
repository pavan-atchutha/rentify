from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('houses/', views.house_list, name='house_list'),
    path('houses/new/', views.house_create, name='house_create'),
    path('houses/<int:house_id>/', views.house_detail, name='house_detail'),
    path('buy/', views.buy_houses, name='buy_houses'),
    path('buy/<int:house_id>/', views.buy_house1, name='buy_house1'),
    path('sell/', views.sell_house, name='sell_house'),
    path('logout/', views.logout_view, name='logout'),
    path('myhousetosell/', views.myhousetosell, name='myhousetosell'),
    path('myhousetosell/<int:house_id>', views.sell_house1, name='sell_house1'),
]
