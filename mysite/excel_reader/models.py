from django.db import models

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length = 10)

class Location(models.Model):
    area = models.ForeignKey(Area)

class Customer(models.Model):
    cust_id = models.IntegerField()
    cust_code = models.IntegerField()

class RCV(models.Model):
    rcv_code = models.CharField(max_length = 14)

class Item(models.Model):
    item_id = models.IntegerField()
    name = models.CharField(max_length=200)
    location = models.ManyToManyField(Location)
    create_date = models.DateTimeField("date created")
    rcv_input = models.OneToOneField(RCV)
    item_code = models.CharField(max_length=40)
    last_out_date = models.DateTimeField("last out date")
    quantity = models.IntegerField()
    quantity_avail = models.IntegerField()

class Excel_Data(models.Model):
    date = models.DateTimeField("date data inputted")
    num_rows = models.IntegerField(default = 0)
    num_columns = models.IntegerField(default = 0)
    items = models.ManyToManyField(Item)