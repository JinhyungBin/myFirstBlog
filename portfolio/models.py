from django.db import models

class Portfolio(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/')
    description=models.CharField(max_length=500)
    
#America
class TravelsA(models.Model):                    
    titleA=models.CharField(max_length=255)
    imageA=models.ImageField(upload_to='images/')
    descriptionA=models.CharField(max_length=500)
#China
class TravelsC(models.Model):                    
    titleC=models.CharField(max_length=255)
    imageC=models.ImageField(upload_to='images/')
    descriptionC=models.CharField(max_length=500)
#Loas
class TravelsL(models.Model):                    
    titleL=models.CharField(max_length=255)
    imageL=models.ImageField(upload_to='images/')
    descriptionL=models.CharField(max_length=500)

def __str__(self):
    return self.title

