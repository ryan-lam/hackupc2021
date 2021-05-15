from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import Profile, Job, Housing

# Create your views here.

def index(request):
    return render(request, "index.html")