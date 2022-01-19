from django.db import models


class Insert(models.Model):
    empresa = models.CharField(max_length=255)
    pontos_ganhos = models.IntegerField()
    pontos_perdidos = models.IntegerField()
    creat_at = models.DateTimeField()

