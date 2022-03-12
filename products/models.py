from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_name = 'menu'
