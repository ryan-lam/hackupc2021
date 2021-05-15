from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import Profile, Job, Housing


# INDEX PAGE
def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if Profile.objects.filter(username=username, password=password).exists():
            request.session["username"] = username
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            return render (request, "index.html", {
                "attempt":True
                })
    
    else: # GET METHOD
        request.session.flush()
        return render(request, "index.html", {
            "attempt":False
        })


# SIGNUP PAGE
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        name = request.POST["name"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        uni_name = request.POST["uni_name"]
        major = request.POST["major"]
        gpa = request.POST["gpa"]

        try:
            profile = Profile(name=name, age=age, gender=gender, major=major, uni_name=uni_name, email=email, password=password, gpa=gpa)
            profile.save()
            request.session["username"] = username
            return HttpResponseRedirect(reverse("dashboard"))
        except:
            return render(request, "signup.html", {
                "attempt":True
            })

    else: # GET METHOD
        return render(request, "signup.html", {
            "attempt":False
        })









def signup(request):
    pass