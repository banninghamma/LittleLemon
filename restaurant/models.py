from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    booking_date = models.DateField()
    no_of_guests = models.IntegerField(null=False)
    booking_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.first_name

class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   inventory = models.IntegerField(null=False)
   item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name