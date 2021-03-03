from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from autoGen.models import Notes27Jan

class Notes27JanUpdateView(UpdateView):
    model = Notes27Jan
    fields = '__all__'
    template_name = "notes27_jan/notes27_jan_update.html"
    success_url = reverse_lazy('notes27_jan_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    #===
    #===
        context.update({
            'template_name' : "notes27_jan/notes27_jan_update.html",
        })
        return context
