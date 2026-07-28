from django.urls import path
from . import views


urlpatterns = [

    # =====================================
    # HOME
    # =====================================

    path(
        "",
        views.home,
        name="home"
    ),

    # =====================================
    # ADMIN AUTHENTICATION
    # =====================================

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

    # =====================================
    # ADMIN DASHBOARD
    # =====================================

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "admin-dashboard/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),

    # =====================================
    # EVENT CATEGORY
    # =====================================

    path(
        "create-category/",
        views.create_event_category,
        name="create_event_category"
    ),

    path(
        "category-list/",
        views.category_list,
        name="category_list"
    ),

    path(
        "edit-category/<int:id>/",
        views.edit_category,
        name="edit_category"
    ),

    path(
        "delete-category/<int:id>/",
        views.delete_category,
        name="delete_category"
    ),

    # =====================================
    # EVENT
    # =====================================

    path(
        "create-event/",
        views.create_event,
        name="create_event"
    ),

    path(
        "event-list/",
        views.event_list,
        name="event_list"
    ),

    path(
        "event-detail/<int:id>/",
        views.event_detail,
        name="event_detail"
    ),

    path(
        "edit-event/<int:id>/",
        views.edit_event,
        name="edit_event"
    ),

    path(
        "delete-event/<int:id>/",
        views.delete_event,
        name="delete_event"
    ),

    # =====================================
    # EVENT MEMBER
    # =====================================

    path(
        "create-event-member/",
        views.create_event_member,
        name="create_event_member"
    ),

    path(
        "event-member-list/",
        views.event_member_list,
        name="event_member_list"
    ),

    # =====================================
    # EVENT WISH
    # =====================================

    path(
        "create-event-wish/",
        views.create_event_wish,
        name="create_event_wish"
    ),

    path(
        "event-wish-list/",
        views.event_wish_list,
        name="event_wish_list"
    ),

    # =====================================
    # EVENT WISH USER
    # =====================================

    path(
        "create-event-wish-user/",
        views.create_event_wish_user,
        name="create_event_wish_user"
    ),

    path(
        "event-wish-user-list/",
        views.event_wish_user_list,
        name="event_wish_user_list"
    ),

    # =====================================
    # COMPLETE EVENTS
    # =====================================

    path(
        "complete-event-list/",
        views.complete_event_list,
        name="complete_event_list"
    ),

    # =====================================
    # CONTACT
    # =====================================

    path(
        "contact/",
        views.contact,
        name="contact"
    ),

    # =====================================
    # USERS (ADMIN)
    # =====================================

    path(
        "user-list/",
        views.user_list,
        name="user_list"
    ),

    # =====================================
    # USER AUTHENTICATION
    # =====================================

    path(
        "user/login/",
        views.user_login,
        name="user_login"
    ),

    path(
        "register/",
        views.register_user,
        name="register_user"
    ),

    # =====================================
    # USER EVENTS
    # =====================================

    path(
        "user/events/",
        views.user_event_list,
        name="user_event_list"
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
    "profile/",
    views.user_profile,
    name="user_profile"
),
path(
    "edit-profile/",
    views.edit_profile,
    name="edit_profile"
),
path(
    "change-password/",
    views.change_password,
    name="change_password"
),
]