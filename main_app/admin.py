from django.contrib import admin

# import your models here.
from .models import Titan, Feeding, Eldian



# register model here
admin.site.register(Titan)

admin.site.register(Feeding)

admin.site.register(Eldian)