from rest_framework import serializers
from .models import RoomReservationModel
from datetime import datetime
import uuid


class RoomReservationSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    startTime = serializers.DateTimeField()
    endTime = serializers.DateTimeField()
    roomName = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return RoomReservationModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        parameters = validated_data.get('queryResult').get('parameters')
        startTimeStr = parameters.get('time-period').get('startTime')
        endTimeStr = parameters.get('time-period').get('endTime')
        startTime = datetime.fromisoformat(startTimeStr)
        endTime = datetime.fromisoformat(endTimeStr)
        instance.roomName = list(parameters.get('roomName').keys())[0]
        instance.startTime = startTime
        instance.endTime = endTime
        instance.save()
        return instance
