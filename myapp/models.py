from django.db import models
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    subject=models.CharField(max_length=250)
    message=models.TextField()
    added_on=models.DateTimeField(auto_now_add=True)
    is_approved=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Contact Table"
        
class Table(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    time=models.DateTimeField(auto_created=True,null=True,blank=True)
    person=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Table"
    
class CategoryA(models.Model):
    category_name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_name
    
class ProductA(models.Model):
    product_name=models.CharField(max_length=30)
    category=models.ForeignKey(CategoryA,on_delete=models.CASCADE,default="")
    product_price=models.IntegerField()
    product_detail=models.TextField()
    product_image=models.ImageField()
    
    def __str__(self):
        return self.product_name


class Team(models.Model):
    chef_name=models.CharField(max_length=30)
    chef_designation=models.CharField(max_length=30)
    chef_image=models.ImageField()
    
    def __str__(self):
        return self.chef_name