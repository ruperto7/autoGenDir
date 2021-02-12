from autoGen.views import Notes27JanDeleteView
from autoGen.views import Notes27JanUpdateView
from autoGen.views import Notes27JanDetailView
from autoGen.views import Notes27JanCreateView
from autoGen.views import Notes27JanListView
"""autoGen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Notes27JanListView.as_view(), name='notes27_jan_list'),      
    path('notes27_jan/list/', Notes27JanListView.as_view(), name='notes27_jan_list'),
    path('notes27_jan/create/', Notes27JanCreateView.as_view(), name='notes27_jan_create'),
    path('notes27_jan/detail/<str:pk>/', Notes27JanDetailView.as_view(), name='notes27_jan_detail'),
    #path('notes27_jan/detail/<int:pk>/', Notes27JanDetailView.as_view(), name='notes27jan_detail'),
    path('notes27_jan/update/<str:pk>/', Notes27JanUpdateView.as_view(), name='notes27_jan_update'),
    path('notes27_jan/delete/<str:pk>/', Notes27JanDeleteView.as_view(), name='notes27_jan_delete'),

]

#path('notes27_jan/create/', Notes27JanCreateView.as_view(), name='notes27_jan_create')
#path('notes27_jan/detail/<int:pk>/', Notes27JanDetailView.as_view(), name='notes27_jan_detail')
#path('notes27_jan/update/<int:pk>/', Notes27JanUpdateView.as_view(), name='notes27_jan_update')
#path('notes27_jan/delete/<int:pk>/', Notes27JanDeleteView.as_view(), name='notes27_jan_delete')
