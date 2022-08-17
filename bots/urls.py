from django.urls import path
from . import views


urlpatterns = [
    path("scraping/", views.botView.as_view()),   
]
