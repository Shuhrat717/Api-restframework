from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.blog.v1.urls'))
]