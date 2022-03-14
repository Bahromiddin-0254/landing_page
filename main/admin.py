from django.contrib import admin
from .models import *
# Register your models here.
from django.db import models
from django.utils.html import format_html
from django.forms import Form

@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    def average_date(self,obj):
        result=Date.objects.filter(date=obj.date)
        
        return format_html("<button class=\"btn\">{}</button>",result.first().date) 
    average_date.short_description="O'rtacha sana"
    list_display = ('date','average_date')
admin.site.register(Employee)
admin.site.register(DailyWH)