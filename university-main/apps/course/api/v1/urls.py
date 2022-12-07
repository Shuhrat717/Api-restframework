from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.course.v1.urls'))
]