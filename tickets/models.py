from django.db import models
from django.db.models.enums import Choices
from datetime import date, datetime
import pytz
# Create your models here.

class Screen(models.Model):
    screen_name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.screen_name

seat_choice = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A3', 'A3'),
        ('A4', 'A4'),
        ('A5', 'A5'),
        ('A6', 'A6'),
        ('A7', 'A7'),
        ('A8', 'A8'),
        ('A9', 'A9'),
        ('A10', 'A10'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B3', 'B3'),
        ('B4', 'B4'),
        ('B5', 'B5'),
        ('B6', 'B6'),
        ('B7', 'B7'),
        ('B8', 'B8'),
        ('B9', 'B9'),
        ('B10', 'B10'),
        ('C1', 'C1'),
        ('C2', 'C2'),
        ('C3', 'C3'),
        ('C4', 'C4'),
        ('C5', 'C5'),
        ('C6', 'C6'),
        ('C7', 'C7'),
        ('C8', 'C8'),
        ('C9', 'C9'),
        ('C10', 'C10'),
        ('D1', 'D1'),
        ('D2', 'D2'),
        ('D3', 'D3'),
        ('D4', 'D4'),
        ('D5', 'D5'),
        ('D6', 'D6'),
        ('D7', 'D7'),
        ('D8', 'D8'),
        ('D9', 'D9'),
        ('D10', 'D10'),
        ('E1', 'E1'),
        ('E2', 'E2'),
        ('E3', 'E3'),
        ('E4', 'E4'),
        ('E5', 'E5'),
        ('E6', 'E6'),
        ('E7', 'E7'),
        ('E8', 'E8'),
        ('E9', 'E9'),
        ('E10', 'E10'),
        ('F1', 'F1'),
        ('F2', 'F2'),
        ('F3', 'F3'),
        ('F4', 'F4'),
        ('F5', 'F5'),
        ('F6', 'F6'),
        ('F7', 'F7'),
        ('F8', 'F8'),
        ('F9', 'F9'),
        ('F10', 'F10'),
        ('G1', 'G1'),
        ('G2', 'G2'),
        ('G3', 'G3'),
        ('G4', 'G4'),
        ('G5', 'G5'),
        ('G6', 'G6'),
        ('G7', 'G7'),
        ('G8', 'G8'),
        ('G9', 'G9'),
        ('G10', 'G10'),
    )

class Seat(models.Model):
    seat_id = models.CharField(choices=seat_choice, max_length=4)
    booked = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
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
    screen = models.ForeignKey(Screen, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.show_name + " :  " + str(self.start_time) + " - " + str(self.end_time)
 
class ShowScreen(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('screen', 'show')

    def __str__(self) -> str:
        return self.screen.screen_name + " - " + str(self.show)
    

class Ticket(models.Model):
    username = models.CharField(max_length=60)
    ticket_id = models.CharField(max_length=70, null=True)
    amount = models.FloatField(null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expriry = models.DateTimeField()
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    show = models.OneToOneField(Show, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.username + "'s " + str(self.show)

