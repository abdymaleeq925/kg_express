from django.contrib import admin
from .models import *

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name', 
        'email', 
        )
    list_filter = [
        "first_name"
    ]
    search_fields = (
        "id",
        "first_name",
        "last_name"
    )