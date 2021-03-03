from django.db import models
#from .models  import RawRequest
#import uuid
#from django.forms import model_to_dict
#from django.core.serializers.json import DjangoJSONEncoder
#from django.db.models import Model


class Notes27Jan(models.Model):
    title = models.CharField(max_length=70, blank=True, default='')
    desc = models.CharField(max_length=200, blank=True, default='')
    comment = models.CharField(max_length=200, blank=True, default='')
    comment1 = models.CharField(max_length=200, blank=True, default='')
    comment2 = models.CharField(max_length=200, blank=True, default='')
    comment3 = models.CharField(max_length=200, blank=True, default='')
    comment4 = models.CharField(max_length=200, blank=True, default='')  
    keywords = models.CharField(max_length=200, blank=True, default='')
    #id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True) #models.IntegerField((max_length=200, blank=False, default=''))
    #id=models.IntegerField(auto_created=True, primary_key=True)
    date = models.DateTimeField(auto_now=True)

