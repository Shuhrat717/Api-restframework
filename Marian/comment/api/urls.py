from django.urls import path, include

urlpatterns = [
    path('v1', include('comment.api.v1.urls'))

]
