from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("materia/<slug:id>/", views.materia),
]
