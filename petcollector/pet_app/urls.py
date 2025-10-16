from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('collection/', views.pet_index, name='pet-index'),
    path('collection/<int:pet_id>/', views.pet_detail, name='pet-detail'),
    path('collection/create/', views.PetCreate.as_view(), name='pet-create'),
]