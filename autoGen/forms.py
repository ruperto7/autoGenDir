from django import forms
from django.forms.widgets import NumberInput
#YEAR_CHOICES = ['2021', '2022']

class Notes27JanForm(forms.Form):
    title = forms.CharField(max_length=70 )
    desc = forms.CharField(max_length=200 )
    comment = forms.CharField(max_length=200 )
    comment1 = forms.CharField(max_length=200 )
    comment2 = forms.CharField(max_length=200 )
    comment3 = forms.CharField(max_length=200 )
    comment4 = forms.CharField(max_length=200 )  
    keywords = forms.CharField(max_length=200 )
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))    
    #id = forms.CharField(max_length=100 ) ##default=uuid.uuid4, primary_key=True, blank=True, unique=True, # models.IntegerField((max_length=200, blank=False, default=''))
    #date = models.DateTimeField(auto_now=True)
    #def __str__(self):
    #    return self.id + ' ' + (self.title if (self.title) else "") + ': ' + (self.desc if (self.desc) else "")
    #date = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_CHOICES))
