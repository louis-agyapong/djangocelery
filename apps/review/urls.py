from django.urls import path

from apps.review.views import reveiw_email

app_name = "review"
urlpatterns = [
    path("", reveiw_email, name="email"),
]
