import django.db.models.deletion
from django.db import models


class Client(models.Model):
    company = models.CharField(max_length=255)
    balance = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class PointsHistoric(models.Model):
    earned_points = models.IntegerField()
    spent_points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    client = models.ForeignKey(Client, related_name='points_client', on_delete=django.db.models.deletion.CASCADE, null=False)
