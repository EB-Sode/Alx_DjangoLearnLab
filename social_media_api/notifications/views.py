from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Notification
from .serializers import NotificationSerializer
# from .models import Like, Post
from notifications.models import Notification


# Create your views here.

class NotificationListView(generics.ListAPIView):
    """Fetch user notifications, unread first"""
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(recipient=user).order_by("is_read", "-timestamp")


class MarkNotificationReadView(generics.GenericAPIView):
    """
    Mark a single notification as read
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            notification = Notification.objects.get(pk=pk, recipient=request.user)
            notification.read = True
            notification.save()
            return Response({"detail": "Notification marked as read."}, status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response({"detail": "Notification not found."}, status=status.HTTP_404_NOT_FOUND)