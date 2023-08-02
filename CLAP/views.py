from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CLAPCreateForm

# Create your views here.
class CLAPCreateView(View):
    def get(self, request, *args, **kwargs):
        form = CLAPCreateForm()
        context = {
            'form':form
        }
        return render(request, 'clap_create.html', context)
    