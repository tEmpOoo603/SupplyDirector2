from django.db import models
from django.db.models import CASCADE


class Folder(models.Model):
    name = models.CharField(blank=True, null=False, max_length=256, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subfolders', on_delete=CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.name:
            super().save(*args,**kwargs)
            self.name = f'New Folder {self.id}'
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'folders'
        verbose_name = 'папку'
        verbose_name_plural = 'папки'

class File(models.Model):
    name = models.CharField(blank=False, null=False, max_length=256, unique=True)
    folder = models.ForeignKey(Folder, blank=False, null=False, on_delete=CASCADE, related_name='files')
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'files'
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'
