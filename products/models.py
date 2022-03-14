from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'products_menu'
        
class Category(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'products_category'
    
class Drink(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField

    class Meta:
        db_table = 'products_drink'

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'products_image'
        
class Size(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'products_size'
        
class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'products_nutrition'    

class Allergy(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'products_allergy'

class Allergy_Drink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink =  models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_allergydrink'
        

    



# class Go_to_Home(models.Model):
#     name= models.CharField(max_length=3, help_text='집에 가고싶다')
#     time = models.IntegerField(help_text='몇시간이 걸리시나요??')
#     transfer = models.CharField(help_text='뭐타고 집에 가시나요??')