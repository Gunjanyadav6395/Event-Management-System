from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.utils import timezone

from .models import (
    EventCategory,
    Event,
    EventMember,
    EventWish,
    EventWishUser,
    BudgetFinance,
)

from .forms import (
    EventCategoryForm,
    EventForm,
    EventMemberForm,
    EventWishForm,
    EventWishUserForm,
    ContactForm,
    UserRegisterForm,
    UserProfileForm,
    UserPasswordChangeForm,
    BudgetFinanceForm,
)

def home(request):

    latest_events = Event.objects.filter(
        status=True
    ).order_by("-created_at")[:6]

    context = {

        "latest_events": latest_events,

        "total_events": Event.objects.count(),

        "total_categories": EventCategory.objects.count(),

        "total_members": EventMember.objects.count(),

        "completed_events": Event.objects.filter(
            status=True
        ).count(),

    }

    return render(
        request,
        "user/home.html",
        context,
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

    # Recent data for notifications
    recent_events = Event.objects.filter(
        status=True
    ).order_by("-created_at")[:5]

    recent_categories = EventCategory.objects.filter(
        status="Active"
    ).order_by("-created_at")[:5]

    recent_members = EventMember.objects.filter(
        status=True
    ).order_by("-created_at")[:5]

    # Total notification count
    notification_count = (
        recent_events.count() + 
        recent_categories.count() + 
        recent_members.count()
    )

    context = {

        "total_categories": EventCategory.objects.count(),

        "total_events": Event.objects.count(),

        "participants": EventMember.objects.select_related(
            "user",
            "event"
        ).order_by("-created_at"),

        # NEW: Notification data
        "recent_events": recent_events,
        "recent_categories": recent_categories,
        "recent_members": recent_members,
        "notification_count": notification_count,

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
# EDIT EVENT MEMBER
# ===========================

@login_required
def edit_event_member(request, id):

    member = get_object_or_404(
        EventMember,
        id=id
    )

    if request.method == "POST":

        form = EventMemberForm(
            request.POST,
            instance=member
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Member updated successfully."
            )

            return redirect(
                "event_member_list"
            )

    else:

        form = EventMemberForm(
            instance=member
        )

    return render(
        request,
        "events/edit_event_member.html",
        {
            "form": form,
            "member": member,
        }
    )


# ===========================
# DELETE EVENT MEMBER
# ===========================

@login_required
def delete_event_member(request, id):

    member = get_object_or_404(
        EventMember,
        id=id
    )

    member.delete()

    messages.success(
        request,
        "Member deleted successfully."
    )

    return redirect(
        "event_member_list"
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
# MANAGE EVENT FINANCE
# ===========================

@login_required
def manage_event_finance(request):

    if request.method == "POST":

        form = BudgetFinanceForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Event finance details saved successfully."
            )

            return redirect(
                "manage_event_finance"
            )

    else:

        form = BudgetFinanceForm()

    finances = BudgetFinance.objects.select_related(
        "event"
    ).order_by(
        "-created_at"
    )

    return render(
        request,
        "events/manage_event_finance.html",
        {
            "form": form,
            "finances": finances,
        }
    )
# ===========================
# FINANCIAL REPORTS
# ===========================

@login_required
def financial_reports(request):

    finances = BudgetFinance.objects.select_related(
        "event"
    ).order_by(
        "-created_at"
    )

    total_budget = sum(
        finance.budget for finance in finances
    )

    total_projected_expense = sum(
        finance.projected_expense for finance in finances
    )

    total_actual_expense = sum(
        finance.actual_expense for finance in finances
    )

    total_sponsorship_revenue = sum(
        finance.sponsorship_revenue for finance in finances
    )

    total_balance = (
        total_budget
        + total_sponsorship_revenue
        - total_actual_expense
    )

    return render(
        request,
        "events/financial_reports.html",
        {
            "finances": finances,
            "total_budget": total_budget,
            "total_projected_expense": total_projected_expense,
            "total_actual_expense": total_actual_expense,
            "total_sponsorship_revenue": total_sponsorship_revenue,
            "total_balance": total_balance,
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

    # Normal User → User Contact Page
    if not request.user.is_staff and not request.user.is_superuser:

        return render(
            request,
            "user/user_contact.html",
            {
                "form": form,
            }
        )

    # Admin → Existing Admin Contact Page
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

    wishlist_event_ids = set(

        EventWish.objects.filter(

            user=request.user,

            status=True,

        ).values_list(

            "event_id",

            flat=True

        )

    )

    return render(

        request,

        "user/user_event_detail.html",

        {

            "event": event,

            "registered": registered,

            "wishlist_event_ids": wishlist_event_ids,

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
# USER WISHLIST
# ===========================

@login_required
def add_to_wishlist(request, id):

    event = get_object_or_404(
        Event,
        id=id
    )

    wishlist_item, created = EventWish.objects.get_or_create(
        user=request.user,
        event=event,
        defaults={
            "status": True
        }
    )

    if not created:

        wishlist_item.status = True
        wishlist_item.save()

        messages.info(
            request,
            "Event is already in your wishlist."
        )

    else:

        messages.success(
            request,
            "Event added to your wishlist."
        )

    return redirect(
        "user_event_detail",
        id=event.id
    )


# ===========================
# REMOVE FROM WISHLIST
# ===========================

@login_required
def remove_from_wishlist(request, id):

    event = get_object_or_404(
        Event,
        id=id
    )

    EventWish.objects.filter(
        user=request.user,
        event=event
    ).update(
        status=False
    )

    messages.success(
        request,
        "Event removed from your wishlist."
    )

    return redirect(
        "user_event_detail",
        id=event.id
    )


# ===========================
# MY WISHLIST
# ===========================

@login_required
def my_wishlist(request):

    wishlist = EventWish.objects.filter(
        user=request.user,
        status=True
    ).select_related(
        "event",
        "event__category"
    ).order_by(
        "-created_at"
    )

    return render(
        request,
        "user/my_wishlist.html",
        {
            "wishlist": wishlist
        }
    )
# =====================================
# USER LOGIN
# =====================================

def user_login(request):

    # Agar user already login hai
    if request.user.is_authenticated:
        return redirect("user_event_list")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                f"Welcome back, {user.username}!"
            )

            return redirect("user_event_list")

        messages.error(
            request,
            "Invalid Username or Password."
        )

    return render(
        request,
        "user/user_login.html"
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
# =====================================
# USER PROFILE
# =====================================

@login_required
def user_profile(request):

    total_registered_events = EventMember.objects.filter(
        user=request.user,
        status=True
    ).count()

    total_wishlist = EventWish.objects.filter(
        user=request.user,
        status=True
    ).count()

    context = {

        "total_registered_events": total_registered_events,

        "total_wishlist": total_wishlist,

    }

    return render(

        request,

        "user/user_profile.html",

        context

    )
# =====================================
# EDIT USER PROFILE
# =====================================

@login_required
def edit_profile(request):

    if request.method == "POST":

        form = UserProfileForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect("user_profile")

    else:

        form = UserProfileForm(
            instance=request.user
        )

    return render(

        request,

        "user/edit_user_profile.html",

        {

            "form": form,

        }

    )
# =====================================
# CHANGE PASSWORD
# =====================================

@login_required
def change_password(request):

    if request.method == "POST":

        form = UserPasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                "Password changed successfully."
            )

            return redirect("user_profile")

        else:

            messages.error(
                request,
                "Please correct the errors below."
            )

    else:

        form = UserPasswordChangeForm(
            request.user
        )

    return render(

        request,

        "user/change_password.html",

        {

            "form": form,

        }

    )
# ===========================
# EVENT TICKET
# ===========================

@login_required
def event_ticket(request, id):

    member = get_object_or_404(
        EventMember.objects.select_related(
            "user",
            "event",
        ),
        id=id,
        user=request.user,
        status=True,
    )

    event = member.event

    ticket_number = f"EVT-{member.id:06d}"

    return render(
        request,
        "events/event_ticket.html",
        {
            "member": member,
            "event": event,
            "ticket_number": ticket_number,
        }
    )
# ===========================
# ADMIN QR CODE SCANNER
# ===========================

@login_required
def scan_qr(request):

    # Only Admin / Staff can access QR Scanner

    if not request.user.is_staff and not request.user.is_superuser:

        messages.error(
            request,
            "You are not authorized to access the QR Scanner."
        )

        return redirect("user_event_list")

    return render(
        request,
        "events/scan_qr.html"
    )
# ===========================
# ADMIN TICKET VERIFICATION
# ===========================

@login_required
def verify_ticket(request, ticket_number=None):

    ticket = None
    error = None

    # Only Admin / Staff can access
    if not request.user.is_staff and not request.user.is_superuser:

        return redirect("user_event_list")

    # Ticket number URL se aaye
    if ticket_number:

        try:

            member_id = int(
                ticket_number.replace("EVT-", "")
            )

            ticket = EventMember.objects.select_related(
                "user",
                "event",
                "event__category",
            ).get(
                id=member_id,
                status=True,
            )

        except (
            ValueError,
            EventMember.DoesNotExist
        ):

            error = "Invalid or non-existing ticket."

    # Ticket number form se aaye
    elif request.method == "POST":

        ticket_number = request.POST.get(
            "ticket_number",
            ""
        ).strip()

        if ticket_number:

            try:

                member_id = int(
                    ticket_number.replace("EVT-", "")
                )

                ticket = EventMember.objects.select_related(
                    "user",
                    "event",
                    "event__category",
                ).get(
                    id=member_id,
                    status=True,
                )

            except (
                ValueError,
                EventMember.DoesNotExist
            ):

                error = "Invalid or non-existing ticket."

        else:

            error = "Please enter a ticket number."

    return render(
        request,
        "events/verify_ticket.html",
        {
            "ticket": ticket,
            "error": error,
        }
    )
# ===========================
# ADMIN CHECK-IN TICKET
# ===========================

@login_required
def check_in_ticket(request, id):

    # Only Admin / Staff can access
    if not request.user.is_staff and not request.user.is_superuser:

        return redirect("user_event_list")

    ticket = get_object_or_404(
        EventMember,
        id=id,
        status=True,
    )

    # Prevent duplicate check-in
    if ticket.checked_in:

        messages.warning(
            request,
            "This ticket has already been checked in."
        )

        return redirect(
            "verify_ticket",
            ticket_number=f"EVT-{ticket.id:06d}"
        )

    # Mark attendance
    ticket.checked_in = True
    ticket.checked_in_at = timezone.now()
    ticket.save(
        update_fields=[
            "checked_in",
            "checked_in_at",
        ]
    )

    messages.success(
        request,
        "Ticket verified and participant checked in successfully."
    )

    return redirect(
        "verify_ticket",
        ticket_number=f"EVT-{ticket.id:06d}"
    )