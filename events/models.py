from django.db import models


class EventCategory(models.Model):

    STATUS_CHOICES = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    )

    category_name = models.CharField(max_length=100)

    code = models.CharField(max_length=20, unique=True, default="CAT001")

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