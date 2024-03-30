from django.contrib import admin

from carts.admin import CartTabAdmin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "username"]
    search_fields = ["username", "first_name", "last_name", "email"]
    inlines = [
        CartTabAdmin,
    ]
