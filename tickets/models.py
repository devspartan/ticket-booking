from django.db import models

# Create your models here.
class Ticket(models.Model):
    ticket_no = models.FloatField(null=False)
    seat_no = models.FloatField(null=False)