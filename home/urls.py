from django.urls import path
from home.views import home,about,contact,skill,project

urlpatterns=[
    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('skill/', skill),
    path('project/', project),
]