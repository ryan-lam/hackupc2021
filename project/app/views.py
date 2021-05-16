from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import Profile, Job, Housing, Image
from random import choice


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

def dash(request):
    person = Profile.objects.get(email=request.session["email"])
    suggestions = []
    open_jobs = Job.objects.all()
    for job in open_jobs:
        if person.major == job.type and len(suggestions) < 4:
            suggestions.append(job)
    while len(suggestions) < 4:
        job = choice(open_jobs)
        if job not in suggestions:
            suggestions.append(job)
    print(suggestions)
    return render (request, "dashboard.html", {"person": Profile.objects.get(email=request.session["email"]), "suggestions": suggestions})

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

def houses(request):
    all_houses = Housing.objects.all()
    locations = {}
    for house in all_houses:
        if house.location not in locations:
            locations[house.location] = [house]
        else:
            locations[house.location].append(house)
    return render(request, "houses.html", {'locations': locations, "person": Profile.objects.get(email=request.session["email"])})

def housing(request, id):
    house = Housing.objects.get(id=id)
    images = Image.objects.filter(housing=house)
    return render(request, "house.html", {'images':images, "house":house})

def jobs(request):
    person = Profile.objects.get(email=request.session["email"])
    suggestions = []
    open_jobs = Job.objects.all()
    for job in open_jobs:
        if person.major == job.type and len(suggestions) < 4:
            suggestions.append(job)
    while len(suggestions) < 4:
        job = choice(open_jobs)
        if job not in suggestions:
            suggestions.append(job)
    print(suggestions)
    return render(request, "jobs.html", {"person": Profile.objects.get(email=request.session["email"]), "suggestions": suggestions})

def profile(request):
    return render(request, "profile.html", {"person": Profile.objects.get(email=request.session["email"])})
