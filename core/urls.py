from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("reviews/", include("apps.review.urls", namespace="review")),
]
