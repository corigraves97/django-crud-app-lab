from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet, Playdate
from .forms import PlaydateForm
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
# Add the two imports below
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class Home(LoginView):
    template_name= 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def pet_index(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'collection/index.html', {'pets': pets})

@login_required
def pet_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    playdate_form = PlaydateForm()
    return render(request, 'collection/detail.html', {
        'pet': pet,
        'playdate_form': playdate_form
    })

class PetCreate(LoginRequiredMixin, CreateView):
    model = Pet
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PetUpdate(UpdateView):
    model = Pet
    fields = ['type', 'breed', 'fun_fact', 'age']

class PetDelete(DeleteView):
    model = Pet
    success_url = '/collection/'

@login_required
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

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('pet-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )
