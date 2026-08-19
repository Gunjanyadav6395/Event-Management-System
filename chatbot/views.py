import json

from django.http import JsonResponse
from django.conf import settings

from google import genai


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

        user_message = data.get("message", "").strip()

        if not user_message:
            return JsonResponse(
                {"error": "Message cannot be empty."},
                status=400
            )

        client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=user_message
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