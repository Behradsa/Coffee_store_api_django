from django.db import models


class Coffee(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.IntegerField()
    discount_per = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    rating = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images", null=True)
