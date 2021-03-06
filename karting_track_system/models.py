# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

User._meta.get_field('email')._unique = True

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    client_number = models.CharField(max_length=45)
    sex = models.CharField(max_length=1)
    phone_number = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'client'

@receiver(post_save, sender=User)
def create_or_update_client(sender, instance, created, **kwargs):
    clients = Client.objects.raw('select * from client c where c.email=%s', [instance.email])
    if clients:
        client = clients[0]
        client.user = instance
        instance.client = client
    else:
        instance.client=Client(user=instance, email=instance.email) 
    instance.client.save()


class Kart(models.Model):
    kart_number = models.IntegerField(unique=True)
    kart_model = models.ForeignKey('KartModel', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'kart'


class KartModel(models.Model):
    model = models.CharField(max_length=45)
    power = models.FloatField()
    number_of_seats = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kart_model'


class Lap(models.Model):
    start_time = models.IntegerField()
    end_time = models.IntegerField(blank=True, null=True)
    track = models.ForeignKey('Track', models.DO_NOTHING)
    race_drivers = models.ForeignKey('RaceDrivers', models.DO_NOTHING)
    time = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'lap'


class Race(models.Model):
    date = models.DateField()
    number = models.IntegerField()
    finished = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'race'


class RaceDrivers(models.Model):
    race = models.ForeignKey(Race, models.DO_NOTHING)
    kart = models.ForeignKey(Kart, models.DO_NOTHING)
    client = models.ForeignKey(Client, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'race_drivers'


class Track(models.Model):
    shape = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'track'
        
