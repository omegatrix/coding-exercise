from django.urls import path

from . import views

urlpatterns = [
    path("api/", views.index, name="index"),
    path("api/hello-world/", views.hello_world, name="hello-world"),
]
