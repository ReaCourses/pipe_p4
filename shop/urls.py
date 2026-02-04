from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('first/', first_view, name='first_view'),
    path('second/', second_view, name='second_view'),
    path('clothes/', ClothesListView.as_view(), name='clothes_list_view'),
    path('clothes/<int:pk>/',  ClothesDetailView.as_view(), name='clothes_detail_view'),
    path('clothes/create/', ClothesCreateView.as_view(), name='clothes_create_view'),
    path('clothes/<int:pk>/update/',  ClothesUpdateView.as_view(), name='clothes_update_view'),
    path('clothes/<int:pk>/delete/',  ClothesDeleteView.as_view(), name='clothes_delete_view'), 

    path('login/', login_user, name='login_user'),
    path('registration/', registration_user, name='registration_user'),
    path('logout/', logout_user, name='logout_user'),
    
]
