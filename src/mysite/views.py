from django.views.generic.edit import FormView
from django.contrib import messages

from .forms import FileForm


class CountDocumentAdminView(FormView):
    template_name = "../templates/admin/count_document.html"
    form_class = FileForm
    success_url = "/admin/"

    def form_valid(self, form):
        count = form.count_file(self.request.FILES["file"])
        count_message = "Success! Your document has " + str(count) + " characters."
        messages.success(self.request, count_message)
        return super().form_valid(form)
