from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):  
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country)
    def __str__(self):  
        return self.name

class Procedure(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):  
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City)
    def __str__(self):  
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length = 50)
    hospital = models.ForeignKey(Hospital)
    def __str__(self):  
        return self.name

class Cost(models.Model):
    doctor_id = models.ForeignKey(Doctor)
    procedure_id = models.ForeignKey(Procedure)
    price = models.IntegerField(default=0)

class Patient(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 500)
    city = models.ForeignKey(City)
    country = models.ForeignKey(Country)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1)
    def __str__(self):  
        return self.name
