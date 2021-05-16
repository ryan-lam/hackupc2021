from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("houses", views.houses, name="houses"),
    path("houses/<int:id>", views.housing, name="housing"),
    path("jobs", views.jobs, name="jobs"),
    path("dash", views.dash, name="dash"),
    path("profile", views.profile, name="profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
