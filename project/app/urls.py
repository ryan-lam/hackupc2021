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
    path("logout", views.logout, name="logout"),
    path("houses/logout", views.logout, name="logout"),
    path("houses/dash", views.dash, name="dash"),
    path("houses/jobs", views.jobs, name="jobs"),
    path("houses/profile", views.profile, name="profile"),
    path("job/<str:company>/<str:location>", views.job, name="job"),
    path("houses/job/<str:company>/<str:location>", views.job, name="job"),
    path("job_custom", views.job_custom, name="job_custom")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
