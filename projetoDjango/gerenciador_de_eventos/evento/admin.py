from django.contrib import admin

# Register your models here.

from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'data_inicio', 'data_fim', 'cidade', 'gratuito', 'vagas')
    list_filter = ('tipo', 'cidade', 'gratuito')
