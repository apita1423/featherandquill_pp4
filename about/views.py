from django.shortcuts import render
from .models import About

# Create your views here.

# Code Credit: I Think Therefore I Blog Walkthrough
def about_us(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )