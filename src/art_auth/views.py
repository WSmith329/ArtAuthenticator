from django.shortcuts import render
from django.views import View
from django.urls import reverse

from .models import Art, Authentication, Application, Owner, Ownership


class IndexView(View):
    template_name = "art_auth/index.html"

    def get(self, request):
        owned_art = Art.objects.filter(ownership__owner__isnull=False).distinct()
        art_ownerships = {}

        for a in owned_art:
            art_ownerships[a] = list(a.ownership_set.all())

        return render(request, self.template_name, {'owner_history': art_ownerships})
