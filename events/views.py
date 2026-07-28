from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .models import (
    EventCategory,
    Event,
    EventMember,
    EventWish,
    EventWishUser,
)

from .forms import (
    EventCategoryForm,
    EventForm,
    EventMemberForm,
    EventWishForm,
    EventWishUserForm,
    ContactForm,
    UserRegisterForm,
)

def home(request):

    total_categories = EventCategory.objects.count()

    total_events = Event.objects.count()

    total_members = EventMember.objects.count()

    completed_events = Event.objects.filter(status=True).count()

    latest_events = Event.objects.filter(
        status=True
    ).order_by("-created_at")[:3]

    context = {

        "total_categories": total_categories,

        "total_events": total_events,

        "total_members": total_members,

        "completed_events": completed_events,

        "latest_events": latest_events,

    }

    return render(
        request,
        "user/home.html",
        context
    )
# ===========================
# LOGIN
# ===========================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            messages.success(
                request,
                f"Welcome {user.username}!"
            )

            # Admin
            if user.is_staff or user.is_superuser:

                return redirect("admin_dashboard")

            # Normal User
            else:

                return redirect("user_event_list")

        messages.error(
            request,
            "Invalid Username or Password."
        )

    return render(
        request,
        "login.html"
    )

# ===========================
# LOGOUT
# ===========================

def logout_view(request):

    logout(request)

    messages.success(
        request,
        "Logged out successfully."
    )

    return redirect("home")

# ===========================
# DASHBOARD
# ===========================

# ===========================
# DASHBOARD
# ===========================

@login_required
def dashboard(request):

    context = {

        "total_categories": EventCategory.objects.count(),

        "total_events": Event.objects.count(),

        "completed_events": Event.objects.filter(
            status=True
        ).count(),

        "total_users": User.objects.count(),

        "recent_events": Event.objects.order_by(
            "-created_at"
        )[:5],

    }

    return render(

        request,

        "events/dashboard.html",

        context,

    )


# ===========================
# ADMIN DASHBOARD
# ===========================

@login_required
def admin_dashboard(request):

    context = {

        "total_categories": EventCategory.objects.count(),

        "total_events": Event.objects.count(),

        "participants": EventMember.objects.select_related(
            "user",
            "event"
        ).order_by("-created_at"),

    }

    return render(

        request,

        "events/admin.html",

        context,

    )


# ===========================
# CREATE EVENT CATEGORY
# ===========================

@login_required
def create_event_category(request):

    if request.method == "POST":

        form = EventCategoryForm(

            request.POST,

            request.FILES,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Category created successfully."

            )

            return redirect("category_list")

    else:

        form = EventCategoryForm()

    return render(

        request,

        "events/create_event_category.html",

        {

            "form": form,

        }

    )


# ===========================
# CATEGORY LIST
# ===========================

@login_required
def category_list(request):

    categories = EventCategory.objects.order_by(
        "-created_at"
    )

    return render(

        request,

        "events/event_category.html",

        {

            "categories": categories,

        }

    )


# ===========================
# EDIT CATEGORY
# ===========================

@login_required
def edit_category(request, id):

    category = get_object_or_404(

        EventCategory,

        id=id,

    )

    if request.method == "POST":

        form = EventCategoryForm(

            request.POST,

            request.FILES,

            instance=category,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Category updated successfully."

            )

            return redirect("category_list")

    else:

        form = EventCategoryForm(

            instance=category,

        )

    return render(

        request,

        "events/edit_event_category.html",

        {

            "form": form,

            "category": category,

        }

    )


# ===========================
# DELETE CATEGORY
# ===========================

@login_required
def delete_category(request, id):

    category = get_object_or_404(

        EventCategory,

        id=id,

    )

    category.delete()

    messages.success(

        request,

        "Category deleted successfully."

    )

    return redirect("category_list")

# ===========================
# CREATE EVENT
# ===========================

# ===========================
# CREATE EVENT
# ===========================

@login_required
def create_event(request):

    if request.method == "POST":

        form = EventForm(

            request.POST,

            request.FILES,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Event created successfully."

            )

            return redirect("event_list")

    else:

        form = EventForm()

    return render(

        request,

        "events/create_event.html",

        {

            "form": form,

        }

    )


# ===========================
# EVENT LIST
# ===========================

@login_required
def event_list(request):

    query = request.GET.get("q")

    events = Event.objects.all().order_by(

        "-created_at"

    )

    if query:

        events = events.filter(

            Q(event_name__icontains=query) |
            Q(category__category_name__icontains=query) |
            Q(venue__icontains=query)

        )

    return render(

        request,

        "events/event_list.html",

        {

            "events": events,

            "query": query,

        }

    )


# ===========================
# EDIT EVENT
# ===========================

@login_required
def edit_event(request, id):

    event = get_object_or_404(

        Event,

        id=id,

    )

    if request.method == "POST":

        form = EventForm(

            request.POST,

            request.FILES,

            instance=event,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Event updated successfully."

            )

            return redirect("event_list")

    else:

        form = EventForm(

            instance=event,

        )

    return render(

        request,

        "events/edit_event.html",

        {

            "form": form,

            "event": event,

        }

    )


# ===========================
# DELETE EVENT
# ===========================

@login_required
def delete_event(request, id):

    event = get_object_or_404(

        Event,

        id=id,

    )

    event.delete()

    messages.success(

        request,

        "Event deleted successfully."

    )

    return redirect("event_list")


# ===========================
# EVENT DETAIL
# ===========================

@login_required
def event_detail(request, id):

    event = get_object_or_404(

        Event,

        id=id,

    )

    participants = EventMember.objects.filter(

        event=event

    ).select_related(

        "user"

    )

    context = {

        "event": event,

        "participants": participants,

        "participant_count": participants.count(),

    }

    return render(

        request,

        "events/event_detail.html",

        context,

    )


# ===========================
# CREATE EVENT MEMBER
# ===========================

@login_required
def create_event_member(request):

    if request.method == "POST":

        form = EventMemberForm(

            request.POST,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Participant added successfully."

            )

            return redirect("event_member_list")

    else:

        form = EventMemberForm()

    return render(

        request,

        "events/add_event_member.html",

        {

            "form": form,

        }

    )


# ===========================
# EVENT MEMBER LIST
# ===========================

@login_required
def event_member_list(request):

    members = EventMember.objects.select_related(

        "user",

        "event",

    ).order_by(

        "-created_at"

    )

    return render(

        request,

        "events/joinevent_list.html",

        {

            "members": members,

        }

    )


# ===========================
# CREATE EVENT WISH
# ===========================

@login_required
def create_event_wish(request):

    if request.method == "POST":

        form = EventWishForm(

            request.POST,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Event wish added successfully."

            )

            return redirect("event_wish_list")

    else:

        form = EventWishForm()

    return render(

        request,

        "events/add_event_wish.html",

        {

            "form": form,

        }

    )
@login_required
def event_wish_list(request):

    wishes = EventWish.objects.all()

    return render(
        request,
        "events/event_wish_list.html",
        {
            "wishes": wishes
        }
    )


# ===========================
# CREATE EVENT WISH USER
# ===========================

@login_required
def create_event_wish_user(request):

    if request.method == "POST":

        form = EventWishUserForm(

            request.POST,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Event wish user added successfully."

            )

            return redirect("event_wish_user_list")

    else:

        form = EventWishUserForm()

    return render(

        request,

        "events/add_event_user_wish.html",

        {

            "form": form,

        }

    )


# ===========================
# EVENT WISH USER LIST
# ===========================

@login_required
def event_wish_user_list(request):

    users = EventWishUser.objects.select_related(

        "user",

        "event",

    ).order_by(

        "-created_at"

    )

    return render(

        request,

        "events/event_user_wish_list.html",

        {

            "users": users,

        }

    )


# ===========================
# COMPLETE EVENT LIST
# ===========================

@login_required
def complete_event_list(request):

    events = Event.objects.filter(

        status=True

    ).order_by(

        "-start_date"

    )

    return render(

        request,

        "events/complete_event_list.html",

        {

            "events": events,

        }

    )


# ===========================
# CONTACT
# ===========================

@login_required
def contact(request):

    if request.method == "POST":

        form = ContactForm(

            request.POST,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Your message has been sent successfully."

            )

            return redirect("contact")

    else:

        form = ContactForm()

    return render(

        request,

        "events/contact.html",

        {

            "form": form,

        }

    )


# ===========================
# USER LIST
# ===========================

@login_required
def user_list(request):

    users = User.objects.order_by(

        "id"

    )

    return render(

        request,

        "events/user_list.html",

        {

            "users": users,

        }

    )


# ===========================
# USER EVENT LIST
# ===========================

def user_event_list(request):

    query = request.GET.get("q")

    events = Event.objects.filter(

        status=True

    ).select_related(

        "category"

    ).order_by(

        "start_date"

    )

    if query:

        events = events.filter(

            Q(event_name__icontains=query) |

            Q(category__category_name__icontains=query) |

            Q(venue__icontains=query)

        )

    return render(

        request,

        "user/user_event_list.html",

        {

            "events": events,

            "query": query,

        }

    )


# ===========================
# USER EVENT DETAIL
# ===========================

@login_required
def user_event_detail(request, id):

    event = get_object_or_404(

        Event,

        id=id,

    )

    registered = EventMember.objects.filter(

        user=request.user,

        event=event,

    ).exists()

    return render(

        request,

        "user/user_event_detail.html",

        {

            "event": event,

            "registered": registered,

        }

    )


# ===========================
# REGISTER EVENT
# ===========================

@login_required
def register_event(request, id):

    event = get_object_or_404(

        Event,

        id=id,

    )

    if EventMember.objects.filter(

        user=request.user,

        event=event,

    ).exists():

        messages.warning(

            request,

            "You have already registered for this event."

        )

    else:

        EventMember.objects.create(

            user=request.user,

            event=event,

            status=True,

        )

        messages.success(

            request,

            "Event registration completed successfully."

        )

    return redirect(

        "user_event_detail",

        id=event.id,

    )


# ===========================
# MY REGISTERED EVENTS
# ===========================

@login_required
def my_registered_events(request):

    members = EventMember.objects.filter(

        user=request.user,

        status=True,

    ).select_related(

        "event",

        "event__category",

    ).order_by(

        "-created_at"

    )

    return render(

        request,

        "user/my_registered_events.html",

        {

            "members": members,

        }

    )


# ===========================
# USER REGISTRATION
# ===========================

def register_user(request):

    if request.method == "POST":

        form = UserRegisterForm(

            request.POST,

        )

        if form.is_valid():

            user = form.save()

            login(

                request,

                user,

            )

            messages.success(

                request,

                "🎉 Registration successful! Welcome to EventHub."

            )

            return redirect(

                "user_event_list"

            )

        messages.error(

            request,

            "Please correct the errors below."

        )

    else:

        form = UserRegisterForm()

    return render(

        request,

        "user/user_register.html",

        {

            "form": form,

        }

    )