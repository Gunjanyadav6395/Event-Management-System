from django.urls import path
from . import views

urlpatterns = [

    # Home Page
    path(
    "",
    views.home,
    name="home"
),

    # Login
    path(
    "login/",
    views.login_view,
    name="login"
),

    # Logout
    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    # Dashboard
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    # Remaining URLs...

    # ---------------- EVENT CATEGORY ----------------

    path(
        'create-category/',
        views.create_event_category,
        name='create_event_category'
    ),

    path(
        'category-list/',
        views.category_list,
        name='category_list'
    ),

    path(
        'edit-category/<int:id>/',
        views.edit_category,
        name='edit_category'
    ),

    path(
        'delete-category/<int:id>/',
        views.delete_category,
        name='delete_category'
    ),

    # ---------------- EVENT ----------------

    path(
        'create-event/',
        views.create_event,
        name='create_event'
    ),

    path(
        'event-list/',
        views.event_list,
        name='event_list'
    ),

    path(
        'edit-event/<int:id>/',
        views.edit_event,
        name='edit_event'
    ),
    
    path(
    "event-detail/<int:id>/",
    views.event_detail,
    name="event_detail"
    ),

    path(
        'delete-event/<int:id>/',
        views.delete_event,
        name='delete_event'
    ),

    # ---------------- EVENT MEMBER ----------------

    path(
        'create-event-member/',
        views.create_event_member,
        name='create_event_member'
    ),

    path(
        'event-member-list/',
        views.event_member_list,
        name='event_member_list'
    ),

    # ---------------- EVENT WISH ----------------

    path(
        'create-event-wish/',
        views.create_event_wish,
        name='create_event_wish'
    ),

    path(
        'event-wish-list/',
        views.event_wish_list,
        name='event_wish_list'
    ),

    # ---------------- EVENT WISH USER ----------------

    path(
        'create-event-wish-user/',
        views.create_event_wish_user,
        name='create_event_wish_user'
    ),

    path(
        'event-wish-user-list/',
        views.event_wish_user_list,
        name='event_wish_user_list'
    ),

    path(
    "complete-event-list/",
    views.complete_event_list,
    name="complete_event_list"
),
    path(
    "contact/",
    views.contact,
    name="contact"
),
    path(
    "user-list/",
    views.user_list,
    name="user_list"
),
path(
    'user/events/',
    views.user_event_list,
    name='user_event_list'
),
path(
    "events/<int:id>/",
    views.user_event_detail,
    name="user_event_detail"
),
path(
    "register-event/<int:id>/",
    views.register_event,
    name="register_event"
),
path(
    "my-events/",
    views.my_registered_events,
    name="my_registered_events"
),
path(
    "register/",
    views.register_user,
    name="register_user"
),
]