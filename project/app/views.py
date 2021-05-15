from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import Profile, Job, Housing


# INDEX PAGE
def index(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        if Profile.objects.filter(email=email, password=password).exists(): # CHECK IF USER IN DB
            request.session["email"] = email
            return render (request, "dashboard.html", {"person": Profile.objects.get(email=email)})
        else: # IF USER NOT IN DB
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
        email = request.POST["email"]
        password = request.POST["password"]
        name = request.POST["name"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        uni_name = request.POST["uni_name"]
        major = request.POST["major"]
        gpa = request.POST["gpa"]

        try: # CREATE ACCOUNT
            if Profile.object.filter(email=email).exists(): # CHECK IF EMAIL IS ALREADY USED
                return render(request, "signup.html", {
                "attempt":True, "email":"This email is already in use"
            })
            else: # IF EMAIL IS NOT IN USE
                profile = Profile(name=name, age=age, gender=gender, major=major, uni_name=uni_name, email=email, password=password, gpa=gpa)
                profile.save()
                request.session["email"] = email
                return HttpResponseRedirect(reverse("dashboard"))

        except: # IF UNABLE TO CREATE ACCOUNT
            return render(request, "signup.html", {
                "attempt":True
            })

    else: # GET METHOD
        return render(request, "signup.html", {
            "attempt":False
        })




