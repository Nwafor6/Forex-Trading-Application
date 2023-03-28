from django.db import models

# Create your models here.
class Account(models.Model):
    login = models.PositiveIntegerField()
    equity = models.DecimalField(max_digits=15, decimal_places=2)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    server_name=models.CharField(max_length=30, null=True, blank=True)
    market_watch_time = models.DateTimeField()

    def __str__(self):
        return f"{self.login} | {self.server_name}"