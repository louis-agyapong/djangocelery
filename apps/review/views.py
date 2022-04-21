from django.shortcuts import render
from apps.review.forms import ReviewForm
from django.http import HttpResponse


def reveiw_email(request):
    """
    View for reveiw email.
    """
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.send_mail()
            return HttpResponse("Thank you for your review.")
    else:
        form = ReviewForm()
    return render(request, "review/review.html", {"form": form})
