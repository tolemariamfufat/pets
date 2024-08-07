from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='pets/', null=True, blank=True)


    def __str__(self):
        return self.name
    
class Interest(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="interests")
    email = models.EmailField()
    message = models.TextField(null=True, blank=True)
    date_submited = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.email} interested in {self.pet.name}"
    
    
