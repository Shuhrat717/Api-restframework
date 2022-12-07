from django.urls import path
from .views import AccountRegisterView


urlpatterns = [
    path('register/', AccountRegisterView.as_view())
]