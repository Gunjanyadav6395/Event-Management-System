from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import EventCategory
from django.contrib import messages
from .forms import EventCategoryForm

@login_required
def create_event_category(request):

    if request.method == "POST":

        form = EventCategoryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, "Category Created Successfully")

            return redirect("category_list")

    else:
        form = EventCategoryForm()

    return render(
        request,
        "events/create_event_category.html",
        {
            "form": form
        }
    )
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {
                "error": "Invalid Username or Password"
            })

    return render(request, "login.html")


@login_required
def dashboard(request):
    return render(request, "events/dashboard.html")


@login_required
def admin_dashboard(request):
    return render(request, "events/admin.html")

@login_required
def category_list(request):
    categories = EventCategory.objects.all()
    return render(request, "events/event_category.html", {
        "categories": categories
    })

def logout_view(request):
    logout(request)
    return redirect("login")