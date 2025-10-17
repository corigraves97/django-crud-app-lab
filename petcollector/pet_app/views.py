from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet, Playdate
from .forms import PlaydateForm
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView



class Home(LoginView):
    template_name= 'home.html'

def about(request):
    return render(request, 'about.html')

def pet_index(request):
    pets = Pet.objects.all()
    return render(request, 'collection/index.html', {'pets': pets})

def pet_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    playdate_form = PlaydateForm()
    return render(request, 'collection/detail.html', {
        'pet': pet,
        'playdate_form': playdate_form
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

def add_playdate(request, pet_id):
    form = PlaydateForm(request.POST)
    if form.is_valid():
        new_playdate = form.save(commit=False)
        new_playdate.pet_id = pet_id
        new_playdate.save()
    return redirect('pet-detail', pet_id=pet_id)

class PlaydateUpdate(UpdateView):
    model = Playdate
    fields = ['date', 'friend']
    #success_url = '/collection/'
    # def form_valid(self, form):
    #     #form = PlaydateForm(request.PUT)
    #     if form.is_valid():
    #         edit_playdate = form.save(commit=False)
    #         edit_playdate.pet_id = pet_id
    #         edit_playdate.save()
    #     return redirect('pet-detail', pet_id=pet_id)

class PlaydateDelete(DeleteView):
    model = Playdate
    def get_success_url(self):
        return reverse('pet-detail', kwargs={'pet_id': self.object.pet.id})
