from django import forms
from .models import EventCategory


class EventCategoryForm(forms.ModelForm):
    class Meta:
        model = EventCategory

        fields = [
            "category_name",
            "code",
            "image",
            "priority",
            "status",
            "description",
        ]

        widgets = {
            "category_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Category Name"
            }),

            "code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "CAT001"
            }),

            "image": forms.FileInput(attrs={
                "class": "form-control"
            }),

            "priority": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Description"
            }),
        }