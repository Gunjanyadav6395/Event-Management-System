from .models import (
    EventCategory,
    Event,
    EventMember,
)


def navbar_data(request):

    # ---------------- Recent Notifications ----------------

    recent_events = Event.objects.order_by("-created_at")[:3]

    recent_categories = EventCategory.objects.order_by("-created_at")[:2]

    recent_members = EventMember.objects.select_related(
        "user",
        "event"
    ).order_by("-created_at")[:2]

    notification_count = (
        recent_events.count()
        + recent_categories.count()
        + recent_members.count()
    )

    # ---------------- Chat Dropdown ----------------

    recent_join_members = EventMember.objects.select_related(
        "user",
        "event"
    ).order_by("-created_at")[:5]

    chat_count = recent_join_members.count()

    # ---------------- Return Context ----------------

    return {

        # Notification
        "notification_count": notification_count,
        "recent_events": recent_events,
        "recent_categories": recent_categories,
        "recent_members": recent_members,

        # Chat
        "recent_join_members": recent_join_members,
        "chat_count": chat_count,

    }