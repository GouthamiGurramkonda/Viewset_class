from django.db import models

# Create your models here.
class Product_category(models.Model):
    category_id=models.PositiveIntegerField()
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    category_name=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    Pid=models.PositiveIntegerField()
    Pname=models.CharField(max_length=100)
    Pprice=models.DecimalField(max_digits=8,decimal_places=2)
    Pdate=models.DateField()

    def __str__(self):
        return self.Pname