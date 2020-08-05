from django.db import models


class Lesson(models.Model):
    student = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    online = models.BooleanField()
    additional_info = models.CharField(max_length=300, null=True, blank=True)





