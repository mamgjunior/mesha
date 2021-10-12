from django.contrib import admin
from .models import Obras

# Register your models here.

@admin.register(Obras)
class ObrasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'autor', 'criado_em')
    list_filter = ('autor', 'criado_em')
    search_fields = ('titulo', 'autor')
    ordering = ('-criado_em', 'autor')
