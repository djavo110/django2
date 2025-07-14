from django.db import models

# Create your models here.

class Region(models.Model):
    title = models.CharField(max_length=40)
    context = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class Tuman(models.Model):
    title = models.CharField(max_length=40)
    context = models.TextField(blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    region =    models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class mahalla(models.Model):
    title = models.CharField(max_length=40)
    context = models.TextField(blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)

    def __str__(self):
        return self.title