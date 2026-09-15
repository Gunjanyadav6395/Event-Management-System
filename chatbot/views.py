import json

from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Count

from google import genai

from events.models import (
    Event,
    EventCategory,
    EventMember,
    EventWish,
    BudgetFinance,
)


def get_eventhub_context(request):
    """
    Collect relevant EventHub information from the database
    so Gemini can answer questions specifically about this project.
    """

    context = []

    # ---------------- EVENTS ----------------

    events = (
        Event.objects
        .filter(status=True)
        .select_related("category")
        .annotate(
            registration_count=Count(
                "eventmember",
                filter=None
            )
        )
        .order_by("start_date")
    )

    context.append("EVENTS:")

    if events.exists():
        for event in events:
            context.append(
                f"""
- Event Name: {event.event_name}
  Category: {event.category.category_name}
  Start Date: {event.start_date}
  End Date: {event.end_date}
  Venue: {event.venue}
  Description: {event.description or "No description available"}
  Registrations: {event.registration_count}
"""
            )
    else:
        context.append("No active events are currently available.")

    # ---------------- CATEGORIES ----------------

    categories = EventCategory.objects.filter(
        status="Active"
    ).order_by("priority")

    context.append("\nEVENT CATEGORIES:")

    if categories.exists():
        for category in categories:
            context.append(
                f"""
- Category: {category.category_name}
  Code: {category.code}
  Description: {category.description or "No description available"}
"""
            )
    else:
        context.append("No active categories are currently available.")

    # ---------------- REGISTRATION COUNT ----------------

    total_registrations = EventMember.objects.filter(
        status=True
    ).count()

    context.append(
        f"\nTOTAL ACTIVE REGISTRATIONS: {total_registrations}"
    )

    # ---------------- WISHLIST COUNT ----------------

    total_wishlist = EventWish.objects.filter(
        status=True
    ).count()

    context.append(
        f"TOTAL ACTIVE WISHLIST ENTRIES: {total_wishlist}"
    )

    # ---------------- CURRENT USER ----------------

    if request.user.is_authenticated:
        context.append(
            f"""
CURRENT USER:
Username: {request.user.username}
Is Admin/Staff: {request.user.is_staff}
"""
        )

        # User's registered events
        user_registrations = (
            EventMember.objects
            .filter(
                user=request.user,
                status=True
            )
            .select_related("event")
        )

        context.append("\nCURRENT USER'S REGISTERED EVENTS:")

        if user_registrations.exists():
            for registration in user_registrations:
                context.append(
                    f"- {registration.event.event_name}"
                )
        else:
            context.append(
                "The current user has no active event registrations."
            )

        # User's wishlist
        user_wishlist = (
            EventWish.objects
            .filter(
                user=request.user,
                status=True
            )
            .select_related("event")
        )

        context.append("\nCURRENT USER'S WISHLIST:")

        if user_wishlist.exists():
            for wish in user_wishlist:
                context.append(
                    f"- {wish.event.event_name}"
                )
        else:
            context.append(
                "The current user has no events in their wishlist."
            )

    # ---------------- ADMIN DATA ----------------

    if request.user.is_authenticated and request.user.is_staff:

        budgets = (
            BudgetFinance.objects
            .select_related("event")
            .all()
        )

        context.append("\nBUDGET & FINANCE:")

        if budgets.exists():
            for budget in budgets:
                context.append(
                    f"""
- Event: {budget.event.event_name}
  Budget: {budget.budget}
  Projected Expense: {budget.projected_expense}
  Actual Expense: {budget.actual_expense}
  Sponsorship Revenue: {budget.sponsorship_revenue}
  Notes: {budget.notes or "No notes"}
"""
                )
        else:
            context.append(
                "No budget and finance records are available."
            )

    return "\n".join(context)


def test_gemini(request):

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Say hello in one short sentence."
    )

    return JsonResponse({
        "response": response.text
    })


def chat_with_gemini(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST requests are allowed."},
            status=405
        )

    try:

        data = json.loads(request.body)

        user_message = data.get(
            "message",
            ""
        ).strip()

        if not user_message:
            return JsonResponse(
                {"error": "Message cannot be empty."},
                status=400
            )

        # Get actual EventHub database information
        eventhub_context = get_eventhub_context(request)

               # ---------------- AI INSTRUCTIONS ----------------

        prompt = f"""
You are EventHub AI - a friendly, conversational assistant for the EventHub event management platform.

IMPORTANT RULES:
1. Answer naturally and conversationally - like a helpful human assistant.
2. Do NOT use any markdown formatting like **bold**, *italics*, or __underline__.
3. Use plain text only with simple formatting like:
   - Numbered lists: 1. First item, 2. Second item
   - Bullet points: - First item, - Second item
   - Line breaks for readability
4. Be warm, professional, and concise (2-4 short paragraphs max).
5. Use the actual EventHub database information provided below.
6. Do not invent any information not present in the data.
7. If data is not available, politely say so.
8. For general/how-to questions, give practical, step-by-step guidance.
9. Add a friendly follow-up question when appropriate.

---------------- EVENTHUB DATABASE INFORMATION ----------------

{eventhub_context}

---------------- END EVENTHUB DATABASE INFORMATION ----------------

CURRENT USER: {request.user.username if request.user.is_authenticated else 'Guest'}

USER QUESTION: {user_message}

Now answer naturally and conversationally. Remember - NO markdown formatting like **bold** or *italics*. Just plain, friendly text.
"""

        client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return JsonResponse({
            "response": response.text
        })

    except json.JSONDecodeError:

        return JsonResponse(
            {"error": "Invalid JSON data."},
            status=400
        )

    except Exception as e:

        return JsonResponse(
            {"error": str(e)},
            status=500
        )