from django.db import models


class Insert(models.Model):
    company = models.CharField(max_length=255)
    earned_points = models.IntegerField()
    spent_points = models.IntegerField()
    # history = models.
    created_at = models.DateTimeField(auto_now_add=True, null=True)

