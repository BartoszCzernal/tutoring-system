from django.db import models


class Lesson(models.Model):
    student = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    online = models.BooleanField()
    additional_info = models.CharField(max_length=300)





