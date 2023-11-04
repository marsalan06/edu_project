import base64
import json
import urllib.parse
from base64 import urlsafe_b64encode

import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ZoomMeeting
from .serializers import ZoomMeetingSerializer


# Create your views here.
# @method_decorator(csrf_exempt, name='get')
class ZoomOAuthRedirectView(View):
    def get(self, request):
        # zoom_authorization_url = f'https://zoom.us/oauth/authorize?response_type=code&client_id={settings.CLIENT_ID}&redirect_uri={settings.REDIRECT_URI}'
        print("=====tittiiittss====")
        zoom_authorization_url = 'https://zoom.us/oauth/authorize?response_type=code&client_id=00nl0kjuR1a9rCH0u83F1A&redirect_uri=http%3A%2F%2F0.0.0.0%3A8000%2Fzoom%2Foauth%2Fcallback'
        redirect(zoom_authorization_url)
        return redirect(zoom_authorization_url)
        # print("======titsd====")
        # return None


class ZoomOAuthCallbackView(View):

    def get(self, request):
        code = request.GET.get('code')
        print("====testing=====")
        print(code)
        token_url = 'https://zoom.us/oauth/token'
        payload = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://0.0.0.0:8000/zoom/oauth/callback'
        }

        # Encode the client ID and client secret
        client_id = '00nl0kjuR1a9rCH0u83F1A'
        client_secret = 'zx5ERBKMamKZc5ibEvdj5nSP7n5cQ6vI'
        # credentials = f'{client_id}:{client_secret}'
        credentials = client_id + ":" + client_secret
        print("-------cred----")
        print(credentials)
        print("========encoded creds=====")
        # print(bytes(credentials,'utf-8'))
        encoded_credentials = base64.b64encode(
            credentials.encode('utf-8')).decode('utf-8')

        print("======encoded crexxxxds encodes====")
        # encoded_credentials = urlsafe_b64encode(bytes(credentials,'utf-8')).decode('utf-8')
        print(encoded_credentials)

        # Set the headers
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")}'
        }

        # Basic MDBubDBranVSMWE5ckNIMHU4M0YxQTp6eDVFUkJLTWFtS1pjNWliRXZkajVuU1A3bjVjUTZ2SQ==
        print(headers)

        # Send the POST request
        response = requests.post(token_url, headers=headers, data=payload)

        # Print the response
        print(response.status_code)
        print(response.json())

        print("========")
        # print(response.json()['access_token'])
        request.session['zoom_access_token'] = response.json()[
            'access_token']

        # print("=========req session token====",
        #       request.session['zoom_access_token'])

        # url = "http://0.0.0.0:8000/zoom/meeting/"

        # payload = json.dumps({
        #     "topic": "test topic 101",
        #     "start_time": "2023-11-05T14:00:00Z",
        #     "duration": "60",
        #     "access_token": request.session['zoom_access_token'],
        # })
        # headers = {
        #     'Content-Type': 'application/json'
        # }

        # response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

        return JsonResponse({"acc_Token": response.json()['access_token']})


class ZoomMeetingAPIView(APIView):

    def post(self, request):
        # access_token = request.data.get('access_token')
        access_token = request.session['zoom_access_token']
        if not access_token:
            return JsonResponse({'error': 'Access token required'}, status=400)

        meeting_url = 'https://api.zoom.us/v2/users/me/meetings'
        payload = {
            'topic': request.data.get('topic'),
            'start_time': request.data.get('start_time'),
            'duration': request.data.get('duration')
        }
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }

        response = requests.post(meeting_url, json=payload, headers=headers)

        if response.status_code == 201:
            meeting_data = response.json()
            return JsonResponse(meeting_data, status=201)
        else:
            # Handle the case where token refresh fails
            return None
