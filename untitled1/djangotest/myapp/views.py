from django.shortcuts import render
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from library.df_response_lib import *
from .models import RoomReservationModel
from datetime import datetime
import json

def home(request):
    
    return HttpResponse('Hello World')

@csrf_exempt
def webhook(request):
    req = json.loads(request.body)
    queryResult = req.get('queryResult')
    action = queryResult.get('action')
    fulfillmentText = {'fulfillmentText': 'This is Django test response from webhook.'}
    parametrs = queryResult.get('parameters')

    if  action == 'room_request_start_end_time':
        date = parametrs.get('date')
        roomName = list(parametrs.get('roomName').keys())[0]
        startTimeStr = parametrs['time-period'].get['startTime']
        endTimeStr = parametrs['time-period'].get['endTime']
        
        startTime = datetime.strptime(startTimeStr, '%Y-%M-%dT%H:%M:%SZ')
        endTime = datetime.strptime(endTimeStr, '%Y-%M-%dT%H:%M:%SZ')
        makeRecord(roomName, startTime, endTime)
        fulfillmentText = 'Suggestion chips Response from webhook'
        aog = actions_on_google_response()
        aog_sr = aog.simple_response([
            [fulfillmentText, fulfillmentText, False]
        ])
        aog_sc = aog.suggestion_chips(["suggestion1", "suggestion2"])
        ff_response = fulfillment_response()
        ff_text = ff_response.fulfillment_text(fulfillmentText)
        ff_messages = ff_response.fulfillment_messages([aog_sr, aog_sc])
        reply = ff_response.main_response(ff_text, ff_messages)
        return JsonResponse(reply, safe=False)
    return JsonResponse(fulfillmentText, safe=False)

def isEnableCreateRecord(room, startTime, endTime):
    return RoomReservationModel.objects.all().filter(startTime < startTime).exists()

def makeRecord(room, startTime, endTime):
    model = RoomReservationModel(room, startTime, endTime)