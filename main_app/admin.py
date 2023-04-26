from django.contrib import admin
from .models import Place, Review, Attraction


# Register your models here.
admin.site.register(Place)

admin.site.register(Review)

admin.site.register(Attraction)