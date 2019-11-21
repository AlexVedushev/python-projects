from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from library.df_response_lib import *
import json

def home(request):
    return HttpResponse('Hello World')

@csrf_exempt
def webhook(request):
    req = json.loads(request.body)
    print(req)
    action = req.get('queryResult').get('action')
    fulfillmentText = {'fulfillmentText': 'This is Django test response from webhook.'}

    if action == 'room_request_with_duration':
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