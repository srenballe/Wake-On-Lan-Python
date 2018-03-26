from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=250)
    mac = models.CharField(max_length=17)

    def __str__(self):
        return self.name

class Broadcast(models.Model):
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.ip
#TODO: There should only be 1 broadcast address at all times, with pk=1 atm.
''' 
    def create(cls, ip):
        if Broadcast.objects.all().count() > 0:
            Broadcast.objects.all().delete()
        else:

'''
