from django.db import models

class Question (models.Model):
    que=models.CharField(max_length=200)
    optiona=models.CharField(max_length=100)
    optionb=models.CharField(max_length=100)
    optionc=models.CharField(max_length=100)
    optiond=models.CharField(max_length=100)
    answer=models.CharField(max_length=1)
    def __str__(self):
        return self.que
        
