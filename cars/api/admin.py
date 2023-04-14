from django.contrib import admin
from .models import Car, Comment, Country, Manufacturer

# Register your models here.
admin.site.register(Car)
admin.site.register(Comment)
admin.site.register(Country)
admin.site.register(Manufacturer)