from django.contrib import admin

from MatchApp.models import mascotas
from MatchApp.models import persona
from MatchApp.models import entrevista
from MatchApp.models import adopciones
from MatchApp.models import seguimiento_adopciones
from MatchApp.models import apadrinamiento
from MatchApp.models import devolucione









# Register your models here.

#admin.site.register(mascotas)
# Define the admin class




class mascotasAdmin(admin.ModelAdmin):
    list_display=('nombre_mascota', 'id_tipo', 'f_registro_matchcota', 'f_nacimiento', 'id_albergue', 'id_estado')
    search_fields = ('nombre_mascota', 'id_estado')
    fieldsets = (
        ('Informacion de la Mascota', {
            'fields': ('nombre_mascota',('id_albergue', 'id_tipo'),('f_registro_matchcota','f_ingreso_albergue'), ('id_estado','numero_carnet'), ('f_nacimiento','f_fallecimiento'),('microchip','activo_web'), 'descripcion','historia')
        }),
        ('Descripcion de la Mascota', {
            'fields': (('sexo', 'id_color'),('tamano_adulto','peso_adulto','tipo_pelo'),('alergias','enfermedad_cronica'),('esterilizado','tratamiento'))
        }),
        ('Puntuacion de la Mascota', {
            'fields': (('relacion_p_hembras','relacion_p_machos','relacion_p_humanos'),('carinoso', 'curioso','deportista'),('educado','independiente','jugueton'),'tranquilo',('sociable_humanos','amigable'),('extrovertido','temeroso','dominante','impulsivo'))
        
        }),
    )

class personaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'email', 'tel_cel', 'f_nacimiento', 'id_distrito')
    search_fields = ('nombre','email')
    fieldsets = (
        ('Sobre el responsable de la Adopcion', {
            'fields': (('nombre','dni'),('sexo','nacionalidad'),('f_nacimiento','email'),('tel_fijo','tel_cel'), ('direccion','id_distrito'), ('ocupacion','centro_trabajo'),('f_registro','f_contacto'), 'comentarios_internos')
        }),
        ('Sobre la Vivienda', {
            'fields': ('tipo_viv',('permiten_mascotas', 'sit_viv'),('seguro_mascotas','rejas_malla'),('ventanas_calle','patio_interno'),('jardin_interno','jardin_externo'),'fumigado')
        }),
        ('Sobre la Familia', {
            'fields': (('tipo_fam','num_persona','ninos'),('alergico_pelo','num_mascotas_actual'),( 'embarazadas','horas_mascota_solo'))
        
        }),
        ('Sobre los intereses del Adoptante', {
            'fields': (('tipo_interes','motivo_adopcion'),('tuvo_mascotas','sit_mascota_anterior'),('conocimiento_cuidados', 'detalle_conocimientos'),('viaje_planeado','detalle_viaje'))
        
        }),
        ('Sobre los responsabilidades del Adoptante', {
            'fields': (('responsable_directo','ambientes_habilitados'))
        
        }),
        ('Sobre el Compromiso', {
            'fields': ('todos_acuerdo',('tiempo_dedicacion','txttiempo'),('compromiso_mudanza', 'txtabandono'),('compromiso_vida','txtvida'),('compromiso_cuidado','txtcuidado1'))
        
        }),
    )

class entrevistaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'id_persona','id_mascotas','f_entrevista', 'resultado', 'puntuacion' )
    search_fields = ('f_entrevista','resultado')
    fieldsets = (
        ('Datos de la Entrevista', {
            'fields': (('id_persona','id_mascotas'),('f_entrevista','id_equipo_matchcota'))
        }),
        ('Resultados de la Entrevista', {
            'fields': (('resultado','puntuacion'),('comentarios_entrevista'))
        }),


     )

class seguimiento_adopcionesInline(admin.TabularInline):
    model = seguimiento_adopciones
    extra = 0

class devolucionesInline(admin.TabularInline):
    model = devolucione
    extra = 0

class adopcionesAdmin(admin.ModelAdmin):
    list_display=('id_entrevista', 'tipo', 'resp_adopcion', 'f_adopcion', 'riesgo_asociado')
    search_fields = ('f_adopcion','tipo')
    fieldsets = (
        ('Adopcion', {
            'fields': (('id_entrevista'),('tipo','f_adopcion'),('resp_adopcion','riesgo_asociado'),('motivo_riesgo'))
        }),
        ('Documentacion de Adopcion', {
            'fields': (('doc_regularizada','resp_regularizacion'),('f_regularizacion','nombre_adoptado'))
        }),
        ('Post-Adopcion', {
            'fields': (('req_etologo','id_etologo'),('comentario'),('concluida','intento_dev'))
        }),
    )
    inlines = [seguimiento_adopcionesInline, devolucionesInline]

class apadrinamientoAdmin(admin.ModelAdmin):
    list_display=('id_persona', 'id_mascotas', 'f_inicio', 'f_fin', 'dia_pago','monto_pactado')
    search_fields = ('id_persona','f_inicio')
    fieldsets = (
        ('DatosAdopcion', {
            'fields': (('id_persona','id_mascotas'),('nom_correos','tipo_ingreso'),('f_inicio','f_fin'))
        }),
        ('Datos del Pago', {
            'fields': (('monto_pactado','dia_pago'),('deb_aut','pag_prom_men'), ('comentarios','reg_trans'))
        }),

    )


class devolucioneAdmin(admin.ModelAdmin):
    list_display=('id_adopcion', 'f_devolucion', 'motivo')
    search_fields = ('id_adopcion', 'f_devolucion')
    fieldsets = (
        ('Devolucion', {
            'fields': (('id_adopcion'),('motivo','f_devolucion'),('comentarios'))
        }),

    )



# Register the admin class with the associated model


admin.site.register(mascotas, mascotasAdmin)
admin.site.register(persona, personaAdmin)
admin.site.register(entrevista, entrevistaAdmin)
admin.site.register(adopciones, adopcionesAdmin)
admin.site.register(apadrinamiento, apadrinamientoAdmin)
admin.site.register(devolucione, devolucioneAdmin)
