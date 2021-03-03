from django import forms
from django.forms.widgets import NumberInput
#YEAR_CHOICES = ['2021', '2022']

class Notes27JanForm(forms.Form):
    title = forms.CharField(max_length=70, help_text =  "ang titulo" )
    #desc = forms.CharField(max_length=200 )
    desc = forms.CharField(widget=forms.Textarea, max_length=200,)
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
"""
from django import forms as f

class MyForm(f.Form):
    name = f.CharField(initial='myInitialname',)

f2 = MyForm(initial={'name': 'MyInstance'}, auto_id=False)
print(f2) #<tr><th>Name:</th><td><input type="text" name="name" value="MyInstance" required></td></tr>
"""
