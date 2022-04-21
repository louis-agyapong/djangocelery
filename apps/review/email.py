from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_review_email(name, email, review):
    context = {
        "name": name,
        "email": email,
        "review": review,
    }
    subject = "Thanks for the review"
    body = render_to_string("review/review_email.txt", context)
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [
        email,
    ]
    email = EmailMessage(subject, body, from_email, recipient_list)
    return email.send(fail_silently=False)
