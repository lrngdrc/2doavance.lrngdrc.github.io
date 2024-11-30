from django.contrib import admin
from .models import razas

# Register your models here.
class razasAdmin(admin.ModelAdmin):
    list_display = ("codigoRazas", "descripcionRazas", "estatus")
admin.site.register(razas, razasAdmin)