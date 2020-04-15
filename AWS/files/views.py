from django.views.generic import CreateView

from .models import Upload


class UploadView(CreateView):
    model = Upload
    fields = ["file"]
    template_name = 'files/upload.html'
    success_url = "/"
