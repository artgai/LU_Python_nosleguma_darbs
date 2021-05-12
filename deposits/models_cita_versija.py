from django.db import models


class Deposit(models.Model):
    deposit = models.FloatField()
    term = models.FloatField()
    rate = models.FloatField()
    interest = models.FloatField(default='0')
