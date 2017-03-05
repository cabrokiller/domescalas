from django.db import models

class Identificador(models.Model):
    codigo = models.CharField(
        max_length=100,
        )
    fecha_ingreso = models.DateField(
        )

class Escala(models.Model):
    identificador = models.ForeignKey(
        Identificador,
        )
    fecha = models.DateField(
        )
    class Meta:
        abstract = True

class Bprs(Escala):
    class Meta:
        verbose_name = 'BPRS'
        verbose_name_plural = 'Escalas BPRS'
    item_01 = models.PositiveSmallIntegerField()
    item_02 = models.PositiveSmallIntegerField()
    item_03 = models.PositiveSmallIntegerField()
    item_04 = models.PositiveSmallIntegerField()
    item_05 = models.PositiveSmallIntegerField()
    item_06 = models.PositiveSmallIntegerField()
    item_07 = models.PositiveSmallIntegerField()
    item_08 = models.PositiveSmallIntegerField()
    item_09 = models.PositiveSmallIntegerField()
    item_10 = models.PositiveSmallIntegerField()
    item_11 = models.PositiveSmallIntegerField()
    item_12 = models.PositiveSmallIntegerField()
    item_13 = models.PositiveSmallIntegerField()
    item_14 = models.PositiveSmallIntegerField()
    item_15 = models.PositiveSmallIntegerField()
    item_16 = models.PositiveSmallIntegerField()
    item_17 = models.PositiveSmallIntegerField()
    item_18 = models.PositiveSmallIntegerField()

class Cgi(Escala):
    class Meta:
        verbose_name = 'escala CGI'
        verbose_name_plural = 'escalas CGI'
    cgi_a = models.PositiveSmallIntegerField()
    cgi_b = models.PositiveSmallIntegerField()

class Eeag(Escala):
    class Meta:
        verbose_name = 'escala EEAG'
        verbose_name_plural = 'escalas EEAG'
    eeag = models.PositiveSmallIntegerField()


#     ##     ## ########  ########   ######
#     ##     ## ##     ## ##     ## ##    ##
#     ##     ## ##     ## ##     ## ##
#     ######### ##     ## ########   ######
#     ##     ## ##     ## ##   ##         ##
#     ##     ## ##     ## ##    ##  ##    ##
#     ##     ## ########  ##     ##  ######
#
class Hdrs(Escala):
    class Meta:
        verbose_name = 'escala Hamilton'
        verbose_name_plural = 'escalas Hamilton'
    item_01 = models.PositiveSmallIntegerField()
    item_02 = models.PositiveSmallIntegerField()
    item_03 = models.PositiveSmallIntegerField()
    item_04 = models.PositiveSmallIntegerField()
    item_05 = models.PositiveSmallIntegerField()
    item_06 = models.PositiveSmallIntegerField()
    item_07 = models.PositiveSmallIntegerField()
    item_08 = models.PositiveSmallIntegerField()
    item_09 = models.PositiveSmallIntegerField()
    item_10 = models.PositiveSmallIntegerField()
    item_11 = models.PositiveSmallIntegerField()
    item_12 = models.PositiveSmallIntegerField()
    item_13 = models.PositiveSmallIntegerField()
    item_14 = models.PositiveSmallIntegerField()
    item_15 = models.PositiveSmallIntegerField()
    item_16 = models.PositiveSmallIntegerField()
    item_17 = models.PositiveSmallIntegerField()

#
#      ######     ##     ##   ##   #####    #####
#      ##   ##    ##     ###  ##  ##   ##  ##   ##
#      ##   ##   ####    ###  ##  ##       ##
#      ######    ## #    ## # ##   #####    #####
#      ##       ######   ## # ##       ##       ##
#      ##       ##   #   ##  ###  ##   ##  ##   ##
#      ##      ###   ##  ##   ##   #####    #####
#
class Panss(Escala):
    class Meta:
        verbose_name = 'PANSS'
        verbose_name_plural = 'Escalas PANSS'

    item_p01 = models.PositiveSmallIntegerField()
    item_p02 = models.PositiveSmallIntegerField()
    item_p03 = models.PositiveSmallIntegerField()
    item_p04 = models.PositiveSmallIntegerField()
    item_p05 = models.PositiveSmallIntegerField()
    item_p06 = models.PositiveSmallIntegerField()
    item_p07 = models.PositiveSmallIntegerField()

    item_n01 = models.PositiveSmallIntegerField()
    item_n02 = models.PositiveSmallIntegerField()
    item_n03 = models.PositiveSmallIntegerField()
    item_n04 = models.PositiveSmallIntegerField()
    item_n05 = models.PositiveSmallIntegerField()
    item_n06 = models.PositiveSmallIntegerField()
    item_n07 = models.PositiveSmallIntegerField()

    item_g01 = models.PositiveSmallIntegerField()
    item_g02 = models.PositiveSmallIntegerField()
    item_g03 = models.PositiveSmallIntegerField()
    item_g04 = models.PositiveSmallIntegerField()
    item_g05 = models.PositiveSmallIntegerField()
    item_g06 = models.PositiveSmallIntegerField()
    item_g07 = models.PositiveSmallIntegerField()
    item_g08 = models.PositiveSmallIntegerField()
    item_g09 = models.PositiveSmallIntegerField()
    item_g10 = models.PositiveSmallIntegerField()
    item_g11 = models.PositiveSmallIntegerField()
    item_g12 = models.PositiveSmallIntegerField()
    item_g13 = models.PositiveSmallIntegerField()
    item_g14 = models.PositiveSmallIntegerField()
    item_g15 = models.PositiveSmallIntegerField()
    item_g16 = models.PositiveSmallIntegerField()

#     ########  ##       ##     ## ########  ######  ##     ## #### ##    ##
#     ##     ## ##       ##     ##    ##    ##    ## ##     ##  ##  ##   ##
#     ##     ## ##       ##     ##    ##    ##       ##     ##  ##  ##  ##
#     ########  ##       ##     ##    ##    ##       #########  ##  #####
#     ##        ##       ##     ##    ##    ##       ##     ##  ##  ##  ##
#     ##        ##       ##     ##    ##    ##    ## ##     ##  ##  ##   ##
#     ##        ########  #######     ##     ######  ##     ## #### ##    ##

class Plutchik_s(Escala):
    class Meta:
        verbose_name = "Escala de Riesgo Suicida de Plutchik"
    item_01 = models.BooleanField()
    item_02 = models.BooleanField()
    item_03 = models.BooleanField()
    item_04 = models.BooleanField()
    item_05 = models.BooleanField()
    item_06 = models.BooleanField()
    item_07 = models.BooleanField()
    item_08 = models.BooleanField()
    item_09 = models.BooleanField()
    item_10 = models.BooleanField()
    item_11 = models.BooleanField()
    item_12 = models.BooleanField()
    item_13 = models.BooleanField()
    item_14 = models.BooleanField()
    item_15 = models.BooleanField()

class Plutchik_v(Escala):
    class Meta:
        verbose_name = "Escala de Riesgo Violencia de Plutchik"
    item_01 = models.PositiveSmallIntegerField()
    item_02 = models.PositiveSmallIntegerField()
    item_03 = models.PositiveSmallIntegerField()
    item_04 = models.PositiveSmallIntegerField()
    item_05 = models.PositiveSmallIntegerField()
    item_06 = models.PositiveSmallIntegerField()
    item_07 = models.PositiveSmallIntegerField()
    item_08 = models.PositiveSmallIntegerField()
    item_09 = models.PositiveSmallIntegerField()
    item_10 = models.PositiveSmallIntegerField()
    item_11 = models.PositiveSmallIntegerField()
    item_12 = models.BooleanField()


class Satisfaccion(Escala):
    class Meta:
        verbose_name = "Escala Satisfacción"
        verbose_name_plural = "Escalas Satisfacción"
    item_1 = models.PositiveSmallIntegerField()
    item_2 = models.PositiveSmallIntegerField()
    item_3 = models.PositiveSmallIntegerField()
    item_4 = models.PositiveSmallIntegerField()
    item_5 = models.PositiveSmallIntegerField()
    item_6 = models.PositiveSmallIntegerField()
    item_7 = models.PositiveSmallIntegerField()
    item_8 = models.PositiveSmallIntegerField()
    item_9 = models.TextField()
    item_10 = models.TextField()

#     ##    ## ##     ## ########   ######
#      ##  ##  ###   ### ##     ## ##    ##
#       ####   #### #### ##     ## ##
#        ##    ## ### ## ########   ######
#        ##    ##     ## ##   ##         ##
#        ##    ##     ## ##    ##  ##    ##
#        ##    ##     ## ##     ##  ######
class Ymrs(Escala):
    class Meta:
        verbose_name = 'escala Young de manía'
        verbose_name_plural = 'escalas Young de manía'
    item_01 = models.PositiveSmallIntegerField()
    item_02 = models.PositiveSmallIntegerField()
    item_03 = models.PositiveSmallIntegerField()
    item_04 = models.PositiveSmallIntegerField()
    item_05 = models.PositiveSmallIntegerField()
    item_06 = models.PositiveSmallIntegerField()
    item_07 = models.PositiveSmallIntegerField()
    item_08 = models.PositiveSmallIntegerField()
    item_09 = models.PositiveSmallIntegerField()
    item_10 = models.PositiveSmallIntegerField()
    item_11 = models.PositiveSmallIntegerField()

class Who_das(Escala):
    class Meta:
        verbose_name = 'escala WHO-DAS'
        verbose_name_plural = 'escalas WHO-DAS'
    test = models.PositiveSmallIntegerField()
# Create your models here.
