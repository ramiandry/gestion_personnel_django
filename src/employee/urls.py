from django.urls import path
from .views import employee

urlpatterns = [
    path("employee/",employee , name="employee" ),
]