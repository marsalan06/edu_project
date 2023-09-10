# urls.py

from django.urls import path, include
from .views import ZoomOAuthCallbackView, ZoomOAuthRedirectView, ZoomMeetingAPIView

# Create a router and register our viewset with it.

urlpatterns = [
    path('oauth/redirect/',ZoomOAuthRedirectView.as_view(),name='zoom_oauth_redirect'),
    path('oauth/callback/',ZoomOAuthCallbackView.as_view(),name='zoom_oauth_callback'),
    path('meeting/',ZoomMeetingAPIView.as_view(),name='zoom-meeting')
]

# GET /call/zoom-meetings/: List all Zoom meetings.
# POST /call/zoom-meetings/: Create a new Zoom meeting.
# GET /call/zoom-meetings/{pk}/: Retrieve details of a specific Zoom meeting.
# PUT /call/zoom-meetings/{pk}/: Update a specific Zoom meeting.
# PATCH /call/zoom-meetings/{pk}/: Partially update a specific Zoom meeting.
# DELETE /call/zoom-meetings/{pk}/: Delete a specific Zoom meeting.