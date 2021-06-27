from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from mantenimientoApp.models import estado
from mantenimientoApp.models import tipo_mascota
from mantenimientoApp.models import albergues
from mantenimientoApp.models import color
from mantenimientoApp.models import medio_contacto
from mantenimientoApp.models import distrito
from Equipo_MatchcotaApp.models import equipo_matchcota
# Create your models here.

E0='0'
E1='1'
E2='2'
E3='3'
E4='4'
E5='5'
E6='6'
E7='7'
E8='8'
E9='9'
E10='10'
puntuacion = (
    (E0, '0'),
	(E1, '1'),
	(E2, '2'),
	(E3, '3'),
	(E4, '4'),
	(E5, '5'),
	(E6, '6'),
	(E7, '7'),
	(E8, '8'),
	(E9, '9'),
	(E10, '10'),
)

U0='0'
U1='1'
U2='2'
U3='0'
U4='0'
U5='0'
U6='0'
U7='0'
U8='0'
U9='0'
U10='0'
U11='0'
U12='0'
U13='0'
U14='0'
U15='0'
U16='0'
U17='0'
U18='0'
U19='0'
U20='0'
U21='0'
U22='0'
U23='0'
U24='0'
U25='0'
U26='0'
U27='0'
U28='0'
U29='0'
U30='0'
U31='0'

dia_mes = (
    (U0, '0'),
	(U1, '1'),
	(U2, '2'),
	(U3, '3'),
	(U4, '4'),
	(U5, '5'),
	(U6, '6'),
	(U7, '7'),
	(U8, '8'),
	(U9, '9'),
	(U10, '10'),
    (U11, '11'),
	(U12, '12'),
	(U13, '13'),
	(U14, '14'),
	(U15, '15'),
	(U16, '16'),
	(U17, '17'),
	(U18, '18'),
	(U19, '19'),
	(U20, '20'),
    (U21, '21'),
	(U22, '22'),
	(U23, '23'),
	(U24, '24'),
	(U25, '25'),
	(U26, '26'),
	(U27, '27'),
	(U28, '28'),
	(U29, '29'),
	(U30, '30'),
    (U31, '31'),
)


SI = 'Si'
NO = 'No'
NA = 'N/A'

activoChoices = (
    (SI,'Si'),
    (NO,'No'),
    (NA,'N/A'),
)

PE='Pequeno'
ME='Mediano'
tamanoChoices = (
    (PE, 'Pequeno'),
	(ME, 'Mediano'),
)
ADOP='Adoptante'
PMAD='Padrino/Madrina'
tipointeresChoices = (
    (ADOP, 'Adoptante'),
	(PMAD, 'Padrino/Madrina'),
)
    
LA= 'Largo'
MED= 'Mediano'
CO= 'Corto'
SP= 'Sin Pelo'
peloChoices= (
        (LA, 'Largo'),
	    (MED, 'Mediano'),
        (CO, 'Corto'),
        (SP, 'Sin Pelo'),
)

MA= 'Macho'
HE= 'Hembra'
sexoChoices= (
        (MA, 'Macho'),
	    (HE, 'Hembra'),
)

CO='Combinado'
UN='Unico'
DA='Directo Albergue'
tipo_apad=(
        (CO,'Combinado'),
        (UN, 'Unico'),
        (DA, 'Directo Albergue'),
)

MAS= 'Hombre'
FE= 'Mujer'
sexoChoices1= (
        (MAS, 'Hombre'),
	    (FE, 'Mujer'),
)

RE= 'Lo regale'
MAN= 'Murio anciano'
MEN= 'Murio de una enfermedad'
PER= 'Se perdio'
m_antChoices1= (
        (RE,'Lo regale'),
        (MAN,'Murio anciano'),
        (MEN,'Murio de una enfermedad'),
        (PER,'Se perdio'),
)

CA= 'Casa'
DE= 'Depa'
t_vivChoices= (
        (CA, 'Casa'),
        (DE, 'Depa'),
)

PR= 'Propia'
AL= 'Alquilada'
s_vivChoices= (
        (PR, 'Propia'),
        (AL, 'Alquilada'),
)

FA= 'Familia'
AD= 'Adulto(s)'
JO= 'Joven <25'
SE= 'Senior'
t_famChoices= (
        (FA, 'Familia'),
        (AD, 'Adulto(s)'),
        (JO, 'Joven <25'),
        (SE, 'Senior'),
)

AP= 'Aprobado'
DP= 'No Aprobado'
res_Choices= (
        (AP, 'Aprobado'),
        (DP, 'No Aprobado'),
)

EM = 'Enfermedad mascota'
PPA = 'Problemas personales del adoptante'
PMA = 'Personalidad mascota'
RCA = 'Relacion con adoptantes'
RCM = 'Relacion con otras mascotas'
OT = 'Otros'
motivo_dev=(
    (EM,'Enfermedad mascota'),
    (PPA,'Problemas personales del adoptante'),
    (PMA,'Personalidad mascota'),
    (RCA,'Relacion con adoptantes'),
    (RCM,'Relacion con otras mascotas'),
    (OT,'Otros'),
)




VO='Voluntario'
SP='Staff permanente'
FU='Fundador'
CO='Contratado'
FS='Fundador/Staff permanente'
condic_Choices=(
        (VO,'Voluntario'),
        (SP,'Staff permanente'),
        (FU,'Fundador'),
        (CO,'Contratado'),
        (FS,'Fundador/Staff permanente'),
)

ADO='Adopción'
INT='Intento'
tipo_adopcion=(
        (ADO,'Adopción'),
        (INT,'Intento'),
)

AL='Alto'
MED='Medio'
BA='Bajo'
riesgo_adopcion=(
        (AL,'Alto'),
        (MED, 'Medio'),
        (BA, 'Bajo'),
)



class mascotas(models.Model):
    numero_carnet=models.CharField(max_length=10,blank=True, null=True, verbose_name='Numero Carnet')
    nombre_mascota=models.CharField(max_length=50, blank=True, null=True, verbose_name='Nombre Mascota')
    id_tipo=models.ForeignKey(
        tipo_mascota, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Tipo de Mascota')
    id_albergue=models.ForeignKey(
        albergues, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Albergue')
    f_registro_matchcota=models.DateField(blank=True, null=True, verbose_name='Fecha Registro en Matchcota')
    f_ingreso_albergue=models.DateField(blank=True, null=True, verbose_name='Fecha Ingreso Albergue')
    id_estado=models.ForeignKey(
        estado, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Estado')
    f_nacimiento=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')
    f_fallecimiento=models.DateField(blank=True, null=True, verbose_name='Fecha de Fallecimiento')
    microchip=models.CharField(max_length=15, blank=True, null=True)
    activo_web=models.CharField(max_length=20,
        choices=activoChoices, blank=True, null=True, verbose_name='Activo en Web')
    sexo=models.CharField(max_length=7,
        choices=sexoChoices, blank=True, null=True)
    id_color=models.ForeignKey(
        color, on_delete=models.CASCADE, blank=True, null=True, verbose_name='color')
    tipo_pelo=models.CharField(max_length=10,
        choices=peloChoices,  blank=True, null=True, verbose_name='tipo de Pelo')
    tamano_adulto=models.CharField(max_length=10,
        choices=tamanoChoices,  blank=True, null=True, verbose_name='Tamano de Adulto')
    peso_adulto=models.IntegerField(blank=True, null=True, verbose_name='Peso de Adulto')
    alergias=models.CharField(max_length=20,
        choices=activoChoices, blank=True, null=True)
    enfermedad_cronica=models.CharField(max_length=20,
        choices=activoChoices,  blank=True, null=True, verbose_name='enfermedad cronica')
    esterilizado=models.CharField(max_length=20,
        choices=activoChoices,  blank=True, null=True)
    tratamiento=models.CharField(max_length=20,
        choices=activoChoices,  blank=True, null=True)
    descripcion=models.CharField(max_length=9000, blank=True, null=True, verbose_name='Descripcion en Web')
    historia=models.CharField(max_length=9000, blank=True, null=True, verbose_name='Historia')
    carinoso=models.CharField(max_length=3,
        choices=puntuacion,  blank=True, null=True, verbose_name='cariñoso')
    curioso=models.CharField(max_length=3,
        choices=puntuacion,  blank=True, null=True)
    deportista=models.CharField(max_length=3,
        choices=puntuacion,  blank=True, null=True)
    educado=models.CharField(max_length=3,
        choices=puntuacion,  blank=True, null=True)
    independiente=models.CharField(max_length=3,
        choices=puntuacion,  blank=True, null=True)
    jugueton=models.CharField(max_length=3,
        choices=puntuacion,  blank=True, null=True)
    tranquilo=models.CharField(max_length=3,
        choices=puntuacion,  blank=True, null=True)
    relacion_p_hembras=models.CharField(max_length=20,
        choices=activoChoices,  blank=True, null=True, verbose_name='Relacon con Hembras')
    relacion_p_machos=models.CharField(max_length=20,
        choices=activoChoices,  blank=True, null=True, verbose_name='Relacion con Machos')
    relacion_p_humanos=models.CharField(max_length=20,
        choices=activoChoices, blank=True, null=True, verbose_name='Relacion con Humanos')
    sociable_humanos=models.CharField(max_length=3,
        choices=activoChoices,  blank=True, null=True, verbose_name='Sociable con Humanos')
    amigable=models.CharField(max_length=3,
        choices=puntuacion, blank=True, null=True)
    extrovertido=models.CharField(max_length=3,
        choices=puntuacion, blank=True, null=True)
    temeroso=models.CharField(max_length=3,
        choices=puntuacion, blank=True, null=True)
    dominante=models.CharField(max_length=3,
        choices=puntuacion, blank=True, null=True)
    impulsivo=models.CharField(max_length=3,
        choices=puntuacion, blank=True, null=True)
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.nombre_mascota


class persona(models.Model):
    id_medio=models.ForeignKey(
        medio_contacto, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Medio de Contacto')
    dni=models.CharField(max_length=20, blank=True, null=True)
    nombre=models.CharField(max_length=100, blank=True, null=True)
    sexo=models.CharField(max_length=10,
        choices=sexoChoices1,  blank=True, null=True)
    nacionalidad=models.CharField(max_length=50, blank=True, null=True)
    f_nacimiento=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')
    email=models.CharField(max_length = 254,blank=True, null=True)
    tel_fijo=models.CharField(max_length=100, blank=True, null=True, verbose_name='telefono fijo')
    tel_cel=models.CharField(max_length=100, blank=True, null=True, verbose_name='Celular')
    ocupacion=models.CharField(max_length=50, blank=True, null=True, verbose_name='Ocupacion')
    centro_trabajo=models.CharField(max_length=60, blank=True, null=True, verbose_name='Centro de Trabajo')
    direccion=models.CharField(max_length=1000, blank=True, null=True, verbose_name='Direccion')
    id_distrito=models.ForeignKey(
        distrito, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Distrito')
    f_registro= models.DateField(blank=True, null=True, verbose_name='Fecha de Registro')
    f_contacto=models.DateField(blank=True, null=True, verbose_name='Fecha de Contacto')
    comentarios_internos=models.CharField(max_length=1000, blank=True, null=True, verbose_name='Comentarios')
    tipo_interes=models.CharField(max_length=40,
        choices=tipointeresChoices, blank=True, null=True, verbose_name='Tipo de Interes')
    tuvo_mascotas= models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Tuvo mascotas')
    conocimiento_cuidados=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Conocimiento de Cuidados')
    sit_mascota_anterior=models.CharField(max_length=50,
        choices=m_antChoices1, blank=True, null=True, verbose_name='Situacion Masc_Ant')
    motivo_adopcion=models.CharField(max_length=1000, blank=True, null=True, verbose_name='Motivo de Adopcion')
    detalle_conocimientos=models.CharField(max_length=3000, blank=True, null=True, verbose_name='Detalle de Conocimientos')
    viaje_planeado=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Viaje Planeado')
    detalle_viaje=models.CharField(max_length=3000, blank=True, null=True, verbose_name='Detalle de Viaje')
    tipo_fam=models.CharField(max_length=20,
        choices=t_famChoices, blank=True, null=True, verbose_name='Tipo de Familia')
    num_persona=models.IntegerField(blank=True, null=True, verbose_name='Numero de Personas')
    alergico_pelo=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Alergico al Pelo')
    embarazadas=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Embarazadas en casa')
    num_mascotas_actual=models.IntegerField(blank=True, null=True, verbose_name='Numero de Mascotas Actual')
    ninos=models.CharField(max_length=3,
        choices=puntuacion, blank=True, null=True, verbose_name='Numero de ninos en casa')
    horas_mascota_solo=models.IntegerField(blank=True, null=True,  verbose_name='Horas mascota solo')
    seguro_mascotas=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Lugar Seguro')
    tipo_viv=models.CharField(max_length=20,
        choices=t_vivChoices, blank=True, null=True, verbose_name='Tipo de Vivienda')
    sit_viv=models.CharField(max_length=30,
        choices=s_vivChoices, blank=True, null=True, verbose_name='Situacion de Vivienda')
    fumigado=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Fumigado')
    permiten_mascotas=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Permiten Mascotas')
    rejas_malla=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Hay rejas/malla')
    ventanas_calle=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Vetanas a la calle')
    ambientes_habilitados=models.CharField(max_length=1000, blank=True, null=True, verbose_name='Ambientes Habilitados')
    jardin_interno=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Jardin interno')
    jardin_externo=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Jardin externo')
    patio_interno=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Patio')
    responsable_directo=models.CharField(max_length=50, blank=True, null=True, verbose_name='Responsable directo')
    todos_acuerdo=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Todos de acuerdo')
    tiempo_dedicacion=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Compromiso de Tiempo de dedicacion')
    compromiso_mudanza=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Compromiso de no Abandono')
    compromiso_vida=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Compromiso Vida')
    compromiso_cuidado=models.CharField(max_length=4,
        choices=activoChoices, blank=True, null=True, verbose_name='Compromiso Cuidado')
    txtacuerdo=models.CharField(max_length=100, blank=True, null=True, verbose_name='Acuerdo')
    txttiempo=models.CharField(max_length=100, blank=True, null=True, verbose_name='Tiempo')
    txtabandono=models.CharField(max_length=100, blank=True, null=True, verbose_name='Abandono')
    txtcuidado1=models.CharField(max_length=100, blank=True, null=True, verbose_name='Cuidado')
    txtvida=models.CharField(max_length=100, blank=True, null=True, verbose_name='Vida')

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
    #   """
        return self.nombre




class entrevista(models.Model):
    nombre=models.CharField(max_length=20, blank=True, null=True, verbose_name='Nombre')
    id_mascotas=models.ForeignKey(
        mascotas, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Mascota')
    id_persona=models.ForeignKey(
        persona, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Entrevistado')
    id_equipo_matchcota=models.ForeignKey(
        equipo_matchcota, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Entrevistador')
    f_entrevista=models.DateField(blank=True, null=True, verbose_name='Fecha de Entrevista')
    resultado=models.CharField(max_length=15,
        choices=res_Choices, blank=True, null=True, verbose_name='Resultado')
    puntuacion=models.CharField(max_length=3, 
        choices=puntuacion,  blank=True, null=True, verbose_name='Puntuacion')
    comentarios_entrevista=models.CharField(max_length=5000, blank=True, null=True, verbose_name='Comentarios')

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id_mascotas,self.id_persona)

@receiver(post_save, sender = entrevista) # Registramos la señal
def set_qr_field(sender, instance, **kwargs):
    # Entramos al if si esta creada la instancia
    if kwargs.get('created'):
        # Actualisamos la instancia
        sender.objects.filter(id = instance.id).update(nombre = 'Ent' + str(instance.id))

    
    
    


class adopciones(models.Model):
    id_entrevista=models.ForeignKey(
        entrevista, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Adopcion')
    nombre_adoptado=models.CharField(max_length=100, blank=True, null=True, verbose_name='Nombre Adoptado')
    tipo=models.CharField(max_length=20,
        choices=tipo_adopcion, blank=True, null=True, verbose_name='Tipo de Proceso')
    resp_adopcion=models.ForeignKey(
        equipo_matchcota, related_name='resp_adopcion+', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Resp Adopcion')
    f_adopcion=models.DateField(blank=True, null=True, verbose_name='Fecha de Adopcion')
    riesgo_asociado=models.CharField(max_length=20,
        choices=riesgo_adopcion, blank=True, null=True, verbose_name='Nivel de riesgo')
    motivo_riesgo=models.CharField(max_length=5000, blank=True, null=True, verbose_name='Motivo de Riesgo')
    doc_regularizada=models.CharField(max_length=20,
        choices=activoChoices, blank=True, null=True, verbose_name='Doc. Regularizada')
    f_regularizacion=models.DateField(blank=True, null=True, verbose_name='Fecha de Adopcion')
    resp_regularizacion=models.ForeignKey(
        equipo_matchcota, related_name='resp_regularizacion+', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Resp Regul.')
    req_etologo=models.CharField(max_length=20,
        choices=activoChoices, blank=True, null=True, verbose_name='Requiere Estologo')
    id_etologo=models.ForeignKey(
        equipo_matchcota, related_name='id_etologo+',on_delete=models.CASCADE, blank=True, null=True, verbose_name='Resp Regul.')
    comentario=models.CharField(max_length=5000, blank=True, null=True, verbose_name='Comentario')
    intento_dev=models.DateField(blank=True, null=True, verbose_name='Fecha Int. Dev')
    concluida=models.CharField(max_length=20,
        choices=activoChoices, blank=True, null=True, verbose_name='Concluida')

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return str(self.id_entrevista)


class seguimiento_adopciones(models.Model):
    id_adopcion=models.ForeignKey(
        adopciones, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Adopcion')
    f_seguimiento=models.DateField(blank=True, null=True, verbose_name='Fecha de Seguimiento')
    comentarios=models.CharField(max_length=5000, blank=True, null=True, verbose_name='Comentario')


class apadrinamiento(models.Model):
    id_persona=models.ForeignKey(
        persona, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Padrino/Madrina')
    nom_correos=models.CharField(max_length=500, blank=True, null=True, verbose_name='Nombre en correo')
    id_mascotas=models.ForeignKey(
        mascotas, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Mascota')
    f_inicio=models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')
    f_fin=models.DateField(blank=True, null=True, verbose_name='Fecha de Fin')
    dia_pago=models.CharField(max_length=20,
        choices=dia_mes, blank=True, null=True, verbose_name='Dia de pago')    
    monto_pactado=models.CharField(max_length=10, blank=True, null=True, verbose_name='Monto Pactado (S/.)')
    tipo_ingreso=models.CharField(max_length=20,
        choices=tipo_apad, blank=True, null=True, verbose_name='Tipo de Ingreso')  
    deb_aut=models.CharField(max_length=20,
        choices=activoChoices, blank=True, null=True, verbose_name='Debito Autom')
    comentarios=models.CharField(max_length=5000, blank=True, null=True, verbose_name='Comentarios')
    reg_trans=models.CharField(max_length=500, blank=True, null=True, verbose_name='Reg. transf')
    pag_prom_men=models.CharField(max_length=10, blank=True, null=True, verbose_name='Pago prom mensual (S/.)')


class devolucione(models.Model):
    id_adopcion=models.ForeignKey(
        adopciones, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Adopcion')
    f_devolucion=models.DateField(blank=True, null=True, verbose_name='Fecha de devolucion')
    comentarios=models.CharField(max_length=5000, blank=True, null=True, verbose_name='Comentarios')
    motivo=models.CharField(max_length=100,
        choices=motivo_dev, blank=True, null=True, verbose_name='Motivo')