from django.views.generic import ListView
from autoGen.models import Notes27Jan
from sortedcontainers import SortedList, SortedSet, SortedDict
from django.http import HttpResponse
import os as o
import json
from django.conf import settings

class Notes27JanListView0(ListView):
    model = Notes27Jan
    #response = HttpResponse("Hello, world. You have class AutoGenInformationView working.")
    queryset = []
    template_name = "notes27_jan/notes27_jan_info.html"

    def showSettings(self):
        astr, adict, alist ="","",""
        for s in dir(settings):
            s2 = getattr(settings, s)
            if (type(s2))==type('x'):
                astr+= s + ' : '+ getattr(settings, s)+'<br>'
            elif (type(s2))==type({'x':0}): 
                #adict+= s + ' : NOT S STRING it is a DICT <br>'
                try:
                    adict+= s+': ' + json.dumps(s2)  +'<br>'
                except:
                    adict+= s + ' : NOT S STRING it is a DICT <br>'   
            elif (type(s2))==type([{'x':0}]):    
                #alist+= s + ' : NOT S STRING it is a LIST <br>'    
                alist+= s +': '+ ''.join((str(e)+"***") for e in s2) + '<br>'   
        return  astr+'<br/><br>'+ adict+'<br/><br>'+alist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#===
#===
        s= self.showSettings()
        context.update({
            'info': 'wazzup',
            #'os':o.__dict__,
            'settings': s ,
        })
        return context



class Notes27JanListView(ListView):
    
    model = Notes27Jan
    template_name = "notes27_jan/notes27_jan_list.html"
    #kw = getObj2(model)
    #qset = model.objects.all() # 
    def getObj2(self,  *args, **kwargs):
        model = Notes27Jan
        allwords = []	
        #allClusters = {}
        for item in model.objects.all(): # .objects.all():
            #allClusters.update({item:item.keywords})
            for word in item.keywords.split(' ') :
                allwords.append(word)
        queryset =     set(allwords)    
        return queryset #set(allwords)  # queryset or context context = super(MyView, self).get_context_data(**kwargs)

    def getObj(self,  *args, **kwargs):
        model = Notes27Jan
        allwords = []	
        #allClusters = {}
        for item in model.objects.all():
            #allClusters.update({item:item.keywords})
            for word in item.keywords.split(' ') :
                allwords.append(word)
        context =     set(allwords)    
        #context = super(Notes27JanListView, self).getObj(**kwargs)
        return context #set(allwords)  # queryset or context context = super(MyView, self).get_context_data(**kwargs)
    #kw = getObj2(model)  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#===
        model = Notes27Jan
        allwordsOnKw = []	
        #allClusters = {}
        for item in model.objects.all():
            #allClusters.update({item:item.keywords})
            for word in item.keywords.split(' ') :
                allwordsOnKw.append(word)
        #newSet =     set(allwords)  
        #newSet = SortedSet(newSet)  
#===
        context.update({
            'keyWordSet': SortedSet(allwordsOnKw),
            'noOfDocs': model.objects.all().count(),
            'noOfKw': len(allwordsOnKw),
        })
        return context
    