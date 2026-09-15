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

    # CHANGE: DateField to DateTimeField (minimal change)
    start_date = models.DateTimeField()  # Changed from DateField

    end_date = models.DateTimeField()    # Changed from DateField

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
    checked_in = models.BooleanField(default=False)

    checked_in_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

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


# ---------------- BUDGET & FINANCE ----------------

class BudgetFinance(models.Model):

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    projected_expense = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    actual_expense = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    sponsorship_revenue = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.event.event_name


# ---------------- NEW: EVENT REGISTRATION (for tickets) ----------------

class EventRegistration(models.Model):
    """Model to track user event registrations with ticket numbers"""
    
    STATUS_CHOICES = (
        ('registered', 'Registered'),
        ('attended', 'Attended'),
        ('cancelled', 'Cancelled'),
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='registrations'
    )
    
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='registrations'
    )
    
    registration_date = models.DateTimeField(auto_now_add=True)
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='registered'
    )
    
    ticket_number = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )
    
    def __str__(self):
        return f"{self.user.username} - {self.event.event_name}"
    
    def save(self, *args, **kwargs):
        if not self.ticket_number:
            import uuid
            self.ticket_number = f"TKT-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)
    
    class Meta:
        unique_together = ['user', 'event']
        ordering = ['-registration_date']