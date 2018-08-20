from django.db import models


# Create your models here.
class IssueTracking(models.Model):
    po = models.CharField(max_length = 50, blank = False)
    date_time = models.DateTimeField()
    def __str__(self):
        return self.po
