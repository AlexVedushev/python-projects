from django.shortcuts import render
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from library.df_response_lib import *
from rest_framework.parsers import JSONParser
from .serializers import RoomReservationSerializer
import json

def home(request):
    return HttpResponse('Hello World')

@csrf_exempt
def webhook(request):
    req = JSONParser().parse(request)
    queryResult = req.get('queryResult')
    action = queryResult.get('action')
    fulfillmentText = {'fulfillmentText': 'This is Django test response from webhook.'}
    parametrs = queryResult.get('parameters')

    if  action == 'room_request_start_end_time':
        # roomName = list(parametrs.get('roomName').keys())[0]
        # startTimeStr = parametrs.get('time-period').get('startTime')
        # endTimeStr = parametrs.get('time-period').get('endTime')
        serializer = RoomReservationSerializer({
            'startTime': parametrs.get('time-period').get('startTime'),
            'endTime': parametrs.get('time-period').get('endTime'),
            'roomName': list(parametrs.get('roomName').keys())[0]
        })
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