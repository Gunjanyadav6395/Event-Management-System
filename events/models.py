from django.db import models
from django.contrib.auth.models import User

# ---------------- EVENT CATEGORY ----------------

class EventCategory(models.Model):

    STATUS_CHOICES = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    )

    category_name = models.CharField(max_length=100)

    code = models.CharField(
        max_length=20,
        unique=True,
        default="CAT001"
    )

    image = models.ImageField(
        upload_to="category_images/",
        blank=True,
        null=True
    )

    priority = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="Active"
    )

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


# ---------------- EVENT ----------------

class Event(models.Model):

    event_name = models.CharField(max_length=200)

    category = models.ForeignKey(
        EventCategory,
        on_delete=models.CASCADE
    )

    start_date = models.DateField()

    end_date = models.DateField()

    venue = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="event_images/",
        blank=True,
        null=True
    )

    priority = models.IntegerField(default=1)

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name


# ---------------- EVENT MEMBER ----------------

class EventMember(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.event_name}"


# ---------------- EVENT WISH ----------------

class EventWish(models.Model):

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.event_name}"


# ---------------- EVENT WISH USER ----------------

class EventWishUser(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.event_name}"

    # ---------------- CONTACT ----------------

class Contact(models.Model):

    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
