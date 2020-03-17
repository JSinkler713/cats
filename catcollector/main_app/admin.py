from django.contrib import admin
# import models that I want to use as the admin
from .models import Cat, Feeding

# Register your models here.
admin.site.register(Cat)
admin.site.register(Feeding)