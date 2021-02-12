from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from autoGen.models import Notes27Jan

class Notes27JanCreateView(CreateView):
    model = Notes27Jan
    fields = '__all__'
    template_name = "notes27_jan/notes27_jan_create.html"
    success_url = reverse_lazy('notes27_jan_list')
