from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "tg_username", "is_active", "is_superuser")
    list_filter = ("tg_username", "is_active")
    search_fields = ("email",)
