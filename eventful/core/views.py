from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

from eventful.core.models import Newsletter


def newsletter_view(request, id):
    newsletter = Newsletter.objects.get(id=id)
    return render(request, 'core/FinalTemplate.html', {"obj": newsletter})
