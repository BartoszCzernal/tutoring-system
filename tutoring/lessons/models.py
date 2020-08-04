from django.db import models


class Lesson(models.Model):
    student = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    additional_info = models.CharField(max_length=300)

    class Meta:
        abstract = True

