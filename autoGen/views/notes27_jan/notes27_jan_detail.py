from django.views.generic import DetailView

from autoGen.models import Notes27Jan


class Notes27JanDetailView(DetailView):
    model = Notes27Jan
    template_name = "notes27_jan/notes27_jan_detail.html"
