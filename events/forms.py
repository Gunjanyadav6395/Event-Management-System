from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import (
    EventCategory,
    Event,
    EventMember,
    EventWish,
    EventWishUser,
    Contact,
    BudgetFinance,
)
# ==========================
# Event Category Form
# ==========================

class EventCategoryForm(forms.ModelForm):

    class Meta:
        model = EventCategory

        fields = [
            "category_name",
            "code",
            "image",
            "priority",
            "status",
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

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "priority": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

        }


# ==========================
# Event Form
# ==========================

class EventForm(forms.ModelForm):

    class Meta:
        model = Event

        fields = [
            "event_name",
            "category",
            "start_date",
            "end_date",
            "venue",
            "description",
            "image",
            "priority",
            "status",
        ]

        widgets = {

            "event_name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "category": forms.Select(attrs={
                "class": "form-select"
            }),

            "start_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "end_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "venue": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "priority": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "status": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),

        }


# ==========================
# Event Member Form
# ==========================

class EventMemberForm(forms.ModelForm):

    class Meta:
        model = EventMember

        fields = [
            "user",
            "event",
            "status",
        ]

        widgets = {

            "user": forms.Select(attrs={
    "class": "form-select",
    "id": "user-select",
}),

"event": forms.Select(attrs={
    "class": "form-select",
    "id": "event-select",
}),

            "status": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["user"].empty_label = "Select User"
        self.fields["event"].empty_label = "Select Event"

        self.fields["user"].label = "User"
        self.fields["event"].label = "Event"
        self.fields["status"].label = "Status"
    
    # ---------------- EVENT WISH USER ----------------

class EventWishUserForm(forms.ModelForm):

    class Meta:
        model = EventWishUser

        fields = [
            "user",
            "event",
            "status",
        ]

        widgets = {

            "user": forms.Select(attrs={
                "class": "form-select"
            }),

            "event": forms.Select(attrs={
                "class": "form-select"
            }),

            "status": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["user"].empty_label = "Select User"
        self.fields["event"].empty_label = "Select Event"

        self.fields["user"].label = "User"
        self.fields["event"].label = "Event"
        self.fields["status"].label = "Status"

    # ---------------- EVENT WISH ----------------

class EventWishForm(forms.ModelForm):

    class Meta:
        model = EventWish

        fields = [
            "user",
            "event",
            "status",
        ]

        widgets = {

            "user": forms.Select(attrs={
                "class": "form-select"
            }),

            "event": forms.Select(attrs={
                "class": "form-select"
            }),

            "status": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["user"].empty_label = "Select User"
        self.fields["event"].empty_label = "Select Event"

        self.fields["user"].label = "User"
        self.fields["event"].label = "Event"
        self.fields["status"].label = "Status"

    # ==========================
# Contact Form
# ==========================

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact

        fields = [
            "full_name",
            "email",
            "subject",
            "message",
        ]

        widgets = {

            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Full Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Email Address"
            }),

            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Subject"
            }),

            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Write your message..."
            }),

        }
# ==========================
# User Profile Form
# ==========================

class UserProfileForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [

            "first_name",

            "last_name",

            "username",

            "email",

        ]

        widgets = {

            "first_name": forms.TextInput(attrs={

                "class": "form-control"

            }),

            "last_name": forms.TextInput(attrs={

                "class": "form-control"

            }),

            "username": forms.TextInput(attrs={

                "class": "form-control"

            }),

            "email": forms.EmailInput(attrs={

                "class": "form-control"

            }),

        }
# ==========================
# User Registration Form
# ==========================

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(

        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Email"
            }
        )

    )

    class Meta:

        model = User

        fields = [

            "username",

            "email",

            "password1",

            "password2",

        ]

        widgets = {

            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Username"
                }
            ),

        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs.update({

            "class": "form-control",
            "placeholder": "Enter Password"

        })

        self.fields["password2"].widget.attrs.update({

            "class": "form-control",
            "placeholder": "Confirm Password"

        })
from django.contrib.auth.forms import PasswordChangeForm


class UserPasswordChangeForm(PasswordChangeForm):

    old_password = forms.CharField(

        widget=forms.PasswordInput(

            attrs={

                "class": "form-control"

            }

        )

    )

    new_password1 = forms.CharField(

        widget=forms.PasswordInput(

            attrs={

                "class": "form-control"

            }

        )

    )

    new_password2 = forms.CharField(

        widget=forms.PasswordInput(

            attrs={

                "class": "form-control"

            }

        )

    )

# ==========================
# Budget & Finance Form
# ==========================

class BudgetFinanceForm(forms.ModelForm):

    class Meta:

        model = BudgetFinance

        fields = [
            "event",
            "budget",
            "projected_expense",
            "actual_expense",
            "sponsorship_revenue",
            "notes",
        ]

        widgets = {

            "event": forms.Select(attrs={
                "class": "form-select"
            }),

            "budget": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Total Budget",
                "step": "0.01"
            }),

            "projected_expense": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Projected Expense",
                "step": "0.01"
            }),

            "actual_expense": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Actual Expense",
                "step": "0.01"
            }),

            "sponsorship_revenue": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Sponsorship Revenue",
                "step": "0.01"
            }),

            "notes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Enter financial notes..."
            }),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["event"].empty_label = "Select Event"
        self.fields["event"].label = "Event"

        self.fields["budget"].label = "Total Budget"
        self.fields["projected_expense"].label = "Projected Expense"
        self.fields["actual_expense"].label = "Actual Expense"
        self.fields["sponsorship_revenue"].label = "Sponsorship Revenue"
        self.fields["notes"].label = "Notes"