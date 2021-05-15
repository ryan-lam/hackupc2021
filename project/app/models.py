from django.db import models


class Profile(models.Model):
    GENDERS = (
        ('M', 'M'),
        ('F', 'F'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDERS)
    major = models.CharField(max_length=64)
    uni_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    gpa = models.FloatField(blank=True, null=True)
    def __str__(self):
        return f"{self.name}, {self.age}, {self.gender}, {self.major}, {self.uni_name}, {self.email}, {self.password}, {self.gpa}"


class Job(models.Model):
    position = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    hourly_pay = models.IntegerField()
    hours = models.IntegerField()
    location = models.CharField(max_length=64)
    application_link = models.CharField(max_length=128, blank=True, null=True)
    def __str__(self):
        return f"{self.position}, {self.company}, {self.description}, {self.hourly_pay}, {self.hours}, {self.location}, {self.application_link}"


class Housing(models.Model):
    address = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    info = models.CharField(max_length=128)
    cost = models.IntegerField()
    images = models.ImageField(upload_to='images/')
    def __str__(self):
        return f"{self.address}, {self.location}, {self.info}, {self.cost}"