from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet

def home(request):
    return HttpResponse('<h1> Welcome to the Pet Collector </h1>')

def about(request):
    return render(request, 'about.html')

def pet_index(request):
    pets = Pet.objects.all()
    return render(request, 'collection/index.html', {'pets': pets})

def pet_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'collection/detail.html', {
        'pet': pet
    })

class PetCreate(CreateView):
    model = Pet
    fields = '__all__'

class PetUpdate(UpdateView):
    model = Pet
    fields = ['type', 'breed', 'fun_fact', 'age']

class PetDelete(DeleteView):
    model = Pet
    success_url = '/collection/'

# Create your views here.
