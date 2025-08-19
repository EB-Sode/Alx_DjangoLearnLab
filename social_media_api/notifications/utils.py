from .models import Notification

def create_notification(recipient, actor, verb, target=None):
    """
    Reusable helper to create notifications.
    """
    # Don’t notify users about their own actions (e.g., liking own post)
    if recipient == actor:
        return None

    return Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target=target
    )
