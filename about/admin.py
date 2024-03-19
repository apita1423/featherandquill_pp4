from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# Code Credit: I Think Therefore I Blog Walkthrough
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)