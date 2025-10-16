from django.db import models
from django.urls import reverse

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    breed = models.CharField(max_length=500)
    fun_fact = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='pet_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('pet-detail', kwargs={'pet_id': self.id})