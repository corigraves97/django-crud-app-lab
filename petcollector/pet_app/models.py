from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


FRIENDS = (
    ('Dug', 'Dug'),
    ('Roz', 'Roz'),
    ('Grandpa', 'Grandpa'),
    ('Spooky', 'Spooky'),
    ('Fig', 'Fig')
)

class Pet(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    breed = models.CharField(max_length=500)
    fun_fact = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='pet_images/', blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('pet-detail', kwargs={'pet_id': self.id})

class Playdate(models.Model):
    date = models.DateField('Playdate Date')
    friend = models.CharField(
        max_length=100,
        choices=FRIENDS,
        default=FRIENDS[0])
    
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.get_friend_display()} on {self.date}'
    
    def get_absolute_url(self):
        print('error', self.id)
        return reverse('pet-detail', kwargs={'pet_id': self.pet_id})
    
    class Meta:
        ordering = ['-date']