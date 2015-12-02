from django.contrib import admin
from .models import pais, ciudad, lenguaje

# Register your models here.

class CiudadInline(admin.TabularInline):
    model = ciudad
    extra = 0

class LenguajeInline(admin.TabularInline):
    model = lenguaje
    extra = 0


class paisAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion General',{'fields': ['Codigo','Nombre','Continente']}),
    ]



admin.site.register(pais,paisAdmin)