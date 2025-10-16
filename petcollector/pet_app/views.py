from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
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

def PetCreate(CreateView):
    model = Pet
    fields = '__all__'


# Create your views here.
