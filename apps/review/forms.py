from django import forms
from apps.review.tasks import send_review_email_task


class ReviewForm(forms.Form):
    """
    Form for reviewing a given review.
    """

    name = forms.CharField(
        label="First name",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Enter your first name",
                "id": "form-name",
            }
        ),
    )
    email = forms.EmailField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Enter your email",
                "id": "form-email",
            }
        ),
    )
    review = forms.CharField(
        label="Review",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your review",
                "id": "form-review",
                "rows": "5",
            }
        ),
    )

    def send_mail(self):
        send_review_email_task.delay(
            self.cleaned_data["name"], self.cleaned_data["email"], self.cleaned_data["review"]
        )
