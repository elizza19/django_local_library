from django.contrib import admin

from mantenimientoApp.models import estado
from mantenimientoApp.models import tipo_mascota
from mantenimientoApp.models import albergues
from mantenimientoApp.models import color
from mantenimientoApp.models import medio_contacto
from mantenimientoApp.models import distrito
from mantenimientoApp.models import detalle_puesto


# Register your models here.

class estadoAdmin(admin.ModelAdmin):
    pass 



class colorAdmin(admin.ModelAdmin):
   pass


class medio_contactoAdmin(admin.ModelAdmin):
    pass



class distritoAdmin(admin.ModelAdmin):
    list_display=('cod_postal','nombre_distrito')


class tipo_mascotaAdmin(admin.ModelAdmin):
    pass

class detalle_puestoAdmin(admin.ModelAdmin):
    pass



class alberguesAdmin(admin.ModelAdmin):
    list_display=('nombre_albergue', 'direccion', 'id_distrito','duena', 'fecha_ingreso_matchcota')

admin.site.register(estado, estadoAdmin)
admin.site.register(color, colorAdmin)
admin.site.register(tipo_mascota, tipo_mascotaAdmin)
admin.site.register(albergues, alberguesAdmin)
admin.site.register(medio_contacto, medio_contactoAdmin)
admin.site.register(distrito, distritoAdmin)
admin.site.register(detalle_puesto,detalle_puestoAdmin)
