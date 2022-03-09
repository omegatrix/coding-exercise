from django.urls import include, path

from solution.views import path_not_found

urlpatterns = [
    path("", include("solution.urls")),
]

handler404 = path_not_found
