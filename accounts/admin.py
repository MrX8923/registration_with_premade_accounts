from django.contrib import admin

from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'age', 'date_joined', 'bio'
    )
    list_filter = (
        'username', 'email'
    )
    list_editable = (
        'date_joined', 'bio'
    )
    search_fields = (
        'username', 'email'
    )
    date_hierarchy = 'date_of_registration'
