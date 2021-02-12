from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from autoGen.models import Notes27Jan

class Notes27JanDeleteView(DeleteView):
    model = Notes27Jan
    template_name = "notes27_jan/notes27_jan_delete.html"
    success_url = reverse_lazy('notes27_jan_list')