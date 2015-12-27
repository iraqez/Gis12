# -*- coding: utf-8 -*-

#from django.db import models
from django.contrib.gis.db import models

class ikk(models.Model):
    koatuu = models.CharField(unique=True,max_length=10)
    koatuu_name = models.CharField(max_length=200)

class kadnums(models.Model):
    cadnum = models.CharField(max_length=22)           # '6822789100:03:010:0064', # сам кадастровий номер
    koatuu = models.ForeignKey(ikk)           # 6822789100, # КОАТУУ (можна примінити розшифровку для розгалудження, і парсингу найбільш необхідних районів в першу чергу)
    zona = models.IntegerField()           # 3, # Кадастрова зона
    kvartal = models.IntegerField()           # 10, # Кадастровий квартал на якому розташована ділянка
    parcel =  models.IntegerField()          #  64, # Номер ділянки
    use =  models.CharField(max_length=5)         #'2.1', # Призначення земельної ділянки по номеру(Десь я знаходив в законі України розписані, який номер для яких цілей)
    purpose = models.CharField(max_length=5)
    unit_area =  models.CharField(max_length=3)       # 'га.                      ', # Одиниці виміру
    area =  models.FloatField()            # '0.5143', # Площа ділянки
    ownershipcode = models.CharField(max_length=4)    # 0, # Код власника (поки побачив, що код 300 це державна власність)
    id_office = models.CharField(max_length=4)         # 608 # тут я не зрозумів, що то, і нашо )))))

class kad_ext_points(models.Model):
    cadnum = models.ForeignKey(kadnums)
    st_xmax =  models.FloatField()   #: '2995036.96228931', # Х-максимальна
    st_ymax =  models.FloatField()     #'6385194.99256115', # Y-максимальна
    st_xmin =  models.FloatField()     #'2994872.30639999', #  Х-мінімальна
    st_ymin =  models.FloatField()     #'6385082.12878709', #  Y-мінімальна

class przem(models.Model):
    num = models.CharField(max_length=5)
    przem = models.TextField()
    type_dzk = models.CharField(max_length=5)

class zona(models.Model):
    koatuu = models.ForeignKey(ikk)
    zona = models.CharField(max_length=2)

class kvartal(models.Model):
    koatuu = models.ForeignKey(ikk)
    zona = models.ForeignKey(zona)
    kvartal = models.CharField(max_length=3)

class fromDzk(models.Model):
    cadnum = models.CharField(max_length=22)           # '6822789100:03:010:0064', # сам кадастровий номер
    koatuu = models.CharField(max_length=10)          # 6822789100, # КОАТУУ (можна примінити розшифровку для розгалудження, і парсингу найбільш необхідних районів в першу чергу)
    zona =   models.CharField(max_length=2)           # 3, # Кадастрова зона
    kvartal = models.CharField(max_length=3)           # 10, # Кадастровий квартал на якому розташована ділянка
    parcel =  models.CharField(max_length=4)          #  64, # Номер ділянки
    use =  models.CharField(max_length=5)         #'2.1', # Призначення земельної ділянки по номеру(Десь я знаходив в законі України розписані, який номер для яких цілей)
    unit_area =  models.CharField(max_length=25)       # 'га.                      ', # Одиниці виміру
    area =  models.FloatField()            # '0.5143', # Площа ділянки
    ownershipcode = models.CharField(max_length=5)    # 0, # Код власника (поки побачив, що код 300 це державна власність)
    id_office = models.CharField(max_length=5)         # 608 # тут я не зрозумів, що то, і нашо )))))
    st_xmax =  models.FloatField()     #: '2995036.96228931', # Х-максимальна
    st_ymax =  models.FloatField()     #'6385194.99256115', # Y-максимальна
    st_xmin =  models.FloatField()     #'2994872.30639999', #  Х-мінімальна
    st_ymin =  models.FloatField()     #'6385082.12878709', #  Y-мінімальна