from django.shortcuts import render
from django.views import generic
from django.urls import reverse

from .models import Art, Authentication, Application


class IndexView(generic.ListView):
    template_name = "art_auth/index.html"
    context_object_name = "application_list"

    def get_queryset(self):
        return Application.objects.all()