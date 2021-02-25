from django.views.generic import ListView
#from django.views import View
#from autoGen.models import Notes27Jan
#from sortedcontainers import SortedList, SortedSet, SortedDict
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from autoGen.models import Notes27Jan

@api_view(['GET'])
class Notes27JanInfoView(ListView): #
    model = Notes27Jan
    fields = '__all__'
    template_name = "notes27_jan/notes27_jan_info.html"
    success_url = reverse_lazy('notes27_jan_info')
    response = HttpResponse("Hello, world. You have class AutoGenInformationView working.")
    def get():
        return HttpResponse("Hello, world. You have class AutoGenInformationView working.")
    
    #def get_queryset():
    #    return ""