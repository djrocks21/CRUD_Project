from django.db import models

# Create your models here.

#-----------------------Session:- 08: Library App---------------------------------------------------

# Book -- id, name, qty, price, is_publised



class Book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    

    def __str__(self):
        return f"{self.__dict__}"



    class Meta:
        db_table = "book"




















