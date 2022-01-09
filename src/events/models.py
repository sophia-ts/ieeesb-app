from django.db import models


class Event(models.Model):
    title = models.CharField(
        max_length=250,
    )
    description = models.CharField(
        max_length=1000,
    )
    date = models.DateTimeField()

    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title
