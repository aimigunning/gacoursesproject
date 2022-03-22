from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=128, unique=True)
    start_date = models.DateField()
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.title
