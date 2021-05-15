from django.contrib import admin
from .models import Profile, Job, Housing, Image

# Register your models here.
admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(Housing)
admin.site.register(Image)

