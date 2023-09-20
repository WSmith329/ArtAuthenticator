from django import forms
from django.core.validators import FileExtensionValidator


class FileForm(forms.Form):
    ALLOWED_EXTENSIONS = ['txt', 'csv', 'json', 'xml', 'py', 'html']

    file = forms.FileField(label="Select a file",
                           validators=[FileExtensionValidator(ALLOWED_EXTENSIONS)])

    def count_file(self, uploaded_file):
        count = 0

        try:
            for chunk in uploaded_file.chunks():
                count += len(chunk.decode("utf-8"))
        except UnicodeDecodeError:
            raise forms.ValidationError("Invalid text encoding", code="invalid_encoding")

        return count - 1
