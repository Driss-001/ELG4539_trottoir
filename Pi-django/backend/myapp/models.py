from django.db import models




class Myapp(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    completed=models.BooleanField(default=False)


    def __str__(self):
 
        #it will return the title
        return self.title
# Create your models here.

class PiState(models.Model):
    RoadState = models.IntegerField(null=True)
    LightState = models.IntegerField(null=True)
    
    def __str__(self):
        return self.title


