from django.db import models

from mantenimientoApp.models import detalle_puesto
from mantenimientoApp.models import distrito

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

class equipo_matchcota(models.Model):
    nombre=models.CharField(max_length = 254,blank=True, null=True, verbose_name='Nombre')
    condicion=models.CharField(max_length=50,
        choices=condic_Choices, blank=True, null=True, verbose_name='Condicion')
    dni=models.CharField(max_length=20, blank=True, null=True)
    id_detalle_puesto=models.ForeignKey(
        detalle_puesto, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Puesto')
    email=models.CharField(max_length = 254,blank=True, null=True, verbose_name='email Personal')
    email_matchcota=models.CharField(max_length = 254,blank=True, null=True, verbose_name='email_Matchcota')
    tel_celular=models.CharField(max_length=100, blank=True, null=True, verbose_name='Telefono celular')
    f_nacimiento=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')
    nacionalidad=models.CharField(max_length=10, blank=True, null=True, verbose_name='telefono fijo')
    direccion=models.CharField(max_length=200, blank=True, null=True, verbose_name='Direccion')
    id_distrito=models.ForeignKey(
        distrito, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Distrito')
    estudios_cursados=models.CharField(max_length=100, blank=True, null=True, verbose_name='Estudios')
    ocupacion=models.CharField(max_length=50, blank=True, null=True, verbose_name='Ocupacion')
    empresa=models.CharField(max_length=100, blank=True, null=True, verbose_name='Empresa')
    t_coche=models.CharField(max_length=20,
        choices=activoChoices, blank=True, null=True, verbose_name='Tiene coche')
    visito_albergue=models.CharField(max_length=20,
        choices=activoChoices, blank=True, null=True, verbose_name='Visito Albergue')
    f_ingreso=models.DateField(blank=True, null=True, verbose_name='Fecha de Ingreso')
    f_cese=models.DateField(blank=True, null=True, verbose_name='Fecha de Cese')

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
    #   """
        return self.nombre

