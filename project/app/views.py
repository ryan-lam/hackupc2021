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
            return HttpResponseRedirect(reverse(dash), {"person": Profile.objects.get(email=email)})
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
    if request.method == "GET":
        house = Housing.objects.get(id=id)
        images = Image.objects.filter(housing=house)
        return render(request, "house.html", {'images':images, "house":house})

def jobs(request):
    person = Profile.objects.get(email=request.session["email"])
    # suggestions = []
    jobs = Job.objects.all()
    # for job in open_jobs:
    #     if person.major == job.type and len(suggestions) < 4:
    #         suggestions.append(job)
    # while len(suggestions) < 4:
    #     job = choice(open_jobs)
    #     if job not in suggestions:
    #         suggestions.append(job)
    # print(suggestions)
    return render(request, "jobs.html", {"person": Profile.objects.get(email=request.session["email"]), "jobs":jobs})

def profile(request):
    return render(request, "profile.html", {"person": Profile.objects.get(email=request.session["email"])})

def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    request.session.flush()
    return HttpResponseRedirect(reverse("index"))
    # return render(request, "index.html", {
    #         "attempt":False
    #     })