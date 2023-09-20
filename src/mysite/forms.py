from django import forms
from django.http import HttpResponseRedirect


class FileForm(forms.Form):
    file = forms.FileField(label="Select a file")

    def count_file(self, uploaded_file):
        count = 0

        for chunk in uploaded_file.chunks():
            count += len(chunk.decode("utf-8"))

        return count
