from django.contrib import admin

from Equipo_MatchcotaApp.models import equipo_matchcota





class equipo_matchcotaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'condicion', 'id_detalle_puesto', 'f_ingreso', 'f_cese')

# Register your models here.

admin.site.register(equipo_matchcota, equipo_matchcotaAdmin)
