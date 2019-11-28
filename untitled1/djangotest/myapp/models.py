from django.db import models
import uuid
# Create your models here.

class RoomReservationModel(models.Model):
    """
    Model room reservation
    """
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = "Unique ID for this reservation")
    startTime = models.DateTimeField(name = "Reservation start time")
    endTime = models.DateTimeField(name = "Reservation end time")
    roomName = models.TextField(name='Room name', default='glassRoom')

    def __init__(self, roomName, startTime, endTime):
        super().__init__()
        self.roomName = roomName
        self.startTime = startTime
        self.endTime = endTime

    def __str__(self):
        return '%s - %s' % (self.startTime, self.endTime)