from django.db import models

# Create your models here.
class Wallet(models.Model):
    wallet_name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to="media")

    def __str__(self):
        return self.wallet_name
