from django.db import models

# Create your models here.
class FoodItem(models.Model):
    order_id = models.AutoField
    item_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="order/images",default= '')

    def __str__(self):
        return self.item_name

