from django.contrib import admin
from .models import Movie, Country, Rate, Category

# Register your models here.
admin.site.register(Movie)
admin.site.register(Country)
admin.site.register(Rate)
admin.site.register(Category)