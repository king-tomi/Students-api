from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from .views import StudentsAPIView, StudentByIDView, StudentByLastNameView, StudentsByLevelView, StudentsByGenderView, StudentsByAgeView, StudentByFirstNameViewUpdate

urlpatterns = [
    path ('', StudentsAPIView.as_view()),
    path('<int:pk>/', StudentByIDView.as_view()),
    path('<str:first_name>/', StudentByFirstNameViewUpdate.as_view()),
    path('<str:last_name>/', StudentByLastNameView.as_view()),
    path('<int:level>/', StudentsByLevelView.as_view()),
    path('<str:gender>/', StudentsByGenderView.as_view()),
    path('<int:age>/', StudentsByAgeView.as_view())
]