from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class Screen(models.Model):
    screen_name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.screen_name

seat_choice = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A3', 'A4'),
        ('A5', 'A5'),
        ('A6', 'A6'),
        ('A7', 'A7'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B3', 'B4'),
        ('B5', 'B5'),
        ('B6', 'B6'),
        ('B7', 'B7'),
        ('C1', 'C1'),
        ('C2', 'C2'),
        ('C3', 'C4'),
        ('C5', 'C5'),
        ('C6', 'C6'),
        ('C7', 'C7'),
        ('D1', 'D1'),
        ('D2', 'D2'),
        ('D3', 'D4'),
        ('D5', 'D5'),
        ('D6', 'D6'),
        ('D7', 'D7'),

    )
class Seat(models.Model):
    seat_id = models.CharField(choices=seat_choice, max_length=4)
    booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_created=True, null=True)
    booked_on = models.DateTimeField(null=True)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('seat_id', 'screen',)
    
    def __str__(self) -> str:
        return self.seat_id + " -> " + str(self.screen)

class Show(models.Model):
    show_name = models.CharField(max_length=60)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ticket_price = models.FloatField()

    def __str__(self) -> str:
        return self.show_name + " :  " + str(self.start_time) + " - " + str(self.end_time)

class ShowScreen(models.Model):
    screen = models.OneToOneField(Screen, on_delete=models.CASCADE)
    show = models.OneToOneField(Show, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.screen

class Ticket(models.Model):
    username = models.CharField(max_length=60)
    ticket_no = models.IntegerField(null=False)
    amount = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_created=True)
    expriry = models.DateTimeField()
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    show = models.OneToOneField(Show, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.username + "'s " + str(self.show)

