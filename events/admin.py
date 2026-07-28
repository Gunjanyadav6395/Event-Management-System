from django.contrib import admin

from .models import (
    EventCategory,
    Event,
    EventMember,
    EventWish,
    EventWishUser,
    Contact,
)


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "category_name",
        "code",
        "priority",
        "status",
        "created_at",
    )

    search_fields = (
        "category_name",
        "code",
    )

    list_filter = (
        "status",
        "created_at",
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "event_name",
        "category",
        "venue",
        "start_date",
        "end_date",
        "status",
    )

    search_fields = (
        "event_name",
        "venue",
    )

    list_filter = (
        "category",
        "status",
    )


@admin.register(EventMember)
class EventMemberAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "event",
        "status",
        "created_at",
    )

    search_fields = (
        "user__username",
        "event__event_name",
    )

    list_filter = (
        "status",
    )


@admin.register(EventWish)
class EventWishAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "event",
        "status",
    )

    search_fields = (
        "user__username",
        "event__event_name",
    )

    list_filter = (
        "status",
    )


@admin.register(EventWishUser)
class EventWishUserAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "event",
        "status",
    )

    search_fields = (
        "user__username",
        "event__event_name",
    )

    list_filter = (
        "status",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "full_name",
        "email",
        "subject",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "subject",
    )

    ordering = (
        "-created_at",
    )