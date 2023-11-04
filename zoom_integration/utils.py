# utils.py

from django.conf import settings
from django.http import JsonResponse
from zoomus import ZoomClient

from zoom_integration.views import ZoomOAuthRedirectView

# def create_zoom_meeting(topic, start_time, duration, timezone):
#     zoom_api_key = settings.ZOOM_KEY
#     zoom_api_secret = settings.ZOOM_SECRET

#     client = ZoomClient(zoom_api_key, zoom_api_secret)

#     # Create a Zoom meeting
#     response = client.meeting.create(user_id='me', topic=topic, start_time=start_time,
#                                      duration=duration, timezone=timezone)

#     if response['status'] == 'success':
#         # Extract the meeting ID and join URL
#         meeting_id = response['id']
#         join_url = response['join_url']

#         return meeting_id, join_url
#     else:
#         # Handle error here (e.g., log or raise an exception)
#         print(f"Error creating Zoom meeting: {response}")
#         return None, None


def call_oauth_method(request):
    obj = ZoomOAuthRedirectView()
    obj.get()
    return JsonResponse("LLLS", safe=False)
