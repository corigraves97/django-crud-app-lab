from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('collection/', views.pet_index, name='pet-index'),
    path('collection/<int:pet_id>/', views.pet_detail, name='pet-detail'),
    path('collection/create/', views.PetCreate.as_view(), name='pet-create'),
    path('collection/<int:pk>/update/', views.PetUpdate.as_view(), name='pet-update'),
    path('collection/<int:pk>/delete/', views.PetDelete.as_view(), name='pet-delete'),
    path('collection/<int:pet_id>/add-playdate/', views.add_playdate, name='add-playdate'),
    path('collection/<int:pet_id>/playdate/<int:pk>/update/', views.PlaydateUpdate.as_view(), name='playdate-update'),
    path('collection/<int:pet_id>/playdate/<int:pk>/delete/', views.PlaydateDelete.as_view(), name='playdate-delete')
]