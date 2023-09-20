from django.views.generic.edit import FormView
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import FileForm


class CountDocumentAdminView(FormView):
    template_name = "../templates/admin/count_document.html"
    form_class = FileForm
    success_url = "/admin/"

    def get(self, request, *args, **kwargs):
        request.session["from"] = request.META.get('HTTP_REFERER', None)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        count = form.count_file(self.request.FILES["file"])
        count_message = "Success! Your document has " + str(count) + " characters."
        messages.success(self.request, count_message)
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.session["from"]:
            self.success_url = request.session["from"]

        return super().post(request, *args, **kwargs)
