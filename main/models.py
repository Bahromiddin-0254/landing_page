from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
from django.contrib.auth import views

class Date(models.Model):
    date=models.DateField("Sana")
    def __str__(self):
        return str(self.date)
    
    class Meta:
        verbose_name="Sana"
        verbose_name_plural="Sana"
        ordering=['date']
class Employee(models.Model):
    date=models.ManyToManyField('Date',through='DailyWH')
    surname=models.CharField("Familiya",max_length=150)
    name=models.CharField("Ism",max_length=150)
    def __str__(self):
        return self.surname+" "+self.name
    class Meta:
        verbose_name="Ishchi"
        verbose_name_plural="Ishchilar"
    @property
    def total(self):
        return self.dailywh_set.all().aggregate(models.Sum('total'))
    @property
    def current(self):
        return self.dailywh_set.all().aggregate(models.Sum('current'))
class DailyWH(models.Model):
    employee=models.ForeignKey('Employee',on_delete=models.CASCADE,null=True,blank=True)
    date=models.ForeignKey('Date',on_delete=models.CASCADE,null=True,blank=True)
    total = models.FloatField("Ishlashi kerak bo'lgan soatlar",default=0)
    current=models.FloatField("Ishlagan soati",default=0)
    
    def __str__(self):
        return self.employee.surname+" "+self.employee.name+" "+str(self.date)
    class Meta:
        verbose_name="Kunlik ish soati"
        verbose_name_plural="Kunlik ish soati"