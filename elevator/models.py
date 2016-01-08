from django.db import models

class elevator(models.Model):
    # cert:'4951',
    # transportTypes:'train,autocar',
    # lat:'51.3278320',lng:'28.8133440',
    # elevatorAddress:'11104, вул. Леніна, буд. 72, м. Овруч, Житомирська обл.',
    # capacity:'14000',shortName:'Овруцька реалбаза хлібопродуктів, ВАТ',
    # fullName:'Відкрите акціонерне товариство \"Овруцька реалізаційна база хлібопродуктів\"',
    # propertyType:'Приватний',
    # propertyTypeCategory:'Інші',
    # loadCapacity:'200',
    # unloadCapacity:'380',
    # odhiRegion:'Житомирська'
    cert = models.CharField(max_length=50)
    transportTypes = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    elevatorAddress = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50)
    shortName = models.CharField(max_length=50)
    fullName = models.CharField(max_length=50)
    propertyType = models.CharField(max_length=50)
    propertyTypeCategory = models.CharField(max_length=50)
    loadCapacity = models.CharField(max_length=50)
    unloadCapacity = models.CharField(max_length=50)
    odhiRegion = models.CharField(max_length=50)
