from django.urls import path
from .views import course_view, course_detail

app_name = 'course'

urlpatterns = [
    path('', course_view, name='list'),
    path('<int:pk>/', course_detail, name='course-detail'),
]
