from django.urls import path, include

urlpatterns = [
    path('v1/', include('contact.api.v1.urls'))
]
