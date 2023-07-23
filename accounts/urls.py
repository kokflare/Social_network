from django.urls import path
from .views import Signuppage

urlpatterns=[
    path('signup/',Signuppage.as_view(), name='signup')
]