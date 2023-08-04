from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model, decorators
from django.utils.translation import gettext_lazy as _

from .models import Newsletter


@admin.register(Newsletter)
class NewletterAdmin(admin.ModelAdmin):
    pass
