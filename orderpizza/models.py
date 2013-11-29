from django.db import models
from pizza import settings

class UnitOrder(models.Model):
    pizza = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField()
    potracheno = models.BooleanField(default=False)
    def __unicode__(self):
        return unicode(self.user)

"""
class TotalOrder(models.Model):
    date = models.DateField()
    orders = models.ForeignKey(UnitOrder)
    boss = models.OneToOneField(settings.AUTH_USER_MODEL)
"""
