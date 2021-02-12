from django import forms


class Notes27JanForm(forms.Form):
    title = forms.CharField(max_length=70 )
    desc = forms.CharField(max_length=200 )
    comment = forms.CharField(max_length=200 )
    comment1 = forms.CharField(max_length=200 )
    comment2 = forms.CharField(max_length=200 )
    comment3 = forms.CharField(max_length=200 )
    comment4 = forms.CharField(max_length=200 )  
    keywords = forms.CharField(max_length=200 )
    id = forms.CharField(max_length=100 ) ##default=uuid.uuid4, primary_key=True, blank=True, unique=True, # models.IntegerField((max_length=200, blank=False, default=''))
    #date = models.DateTimeField(auto_now=True)
    #def __str__(self):
    #    return self.id + ' ' + (self.title if (self.title) else "") + ': ' + (self.desc if (self.desc) else "")
