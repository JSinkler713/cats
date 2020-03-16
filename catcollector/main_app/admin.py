from django.contrib import admin
# import models that I want to use as the admin
from .models import Cat

# Register your models here.
admin.site.register(Cat)