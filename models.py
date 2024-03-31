from django.db import models


class Review(models.Model):
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    title = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return self.name