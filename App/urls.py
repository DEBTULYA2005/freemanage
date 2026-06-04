from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns #allows your API endpoints to accept URLs with optional suffixes like .json or .api, making your API more flexible.
from . import views

urlpatterns = [
    path('students/',views.student_list_create),
    path('timetable/',views.timetable_list_create),
    path('income/', views.income),
    path('students/<int:pk>/', views.student_update_delete),
]

urlpatterns = format_suffix_patterns(urlpatterns)
