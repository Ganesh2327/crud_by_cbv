from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy
class Schoollist(ListView):
    model=School
    context_object_name='SO'


class Schooldetails(DetailView):
    model=School
    context_object_name='DSO'

class Schoolcreate(CreateView):
    model=School
    fields='__all__'


class Schoolupdate(UpdateView):
    model=School
    fields='__all__'

class Schooldelete(DeleteView):
    model=School
    context_object_name='dso'
    success_url=reverse_lazy('Schoollist')