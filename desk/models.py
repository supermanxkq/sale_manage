from django.db import models


class Desk(models.Model):
    name = models.CharField(max_length=10)
    status = models.CharField(max_length=10, default='')
