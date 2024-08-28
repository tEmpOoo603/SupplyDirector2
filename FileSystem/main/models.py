from django.db import models

class Folder(models.Model):
    name = models.CharField(blank=None, max_length=256)
    parent = models.ForeignKey()

