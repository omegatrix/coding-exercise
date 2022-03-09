from django.urls import path

from . import views

urlpatterns = [
    path("api/", views.index, name="index"),
    path("api/hello-world/", views.hello_world, name="hello-world"),
    path("api/add-numbers/<str:num_one>/<str:num_two>", views.add_numbers, name="add-numbers"),
    path("api/join-words/<str:word_one>/<str:word_two>", views.join_words, name="join-words"),
]
