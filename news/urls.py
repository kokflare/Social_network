from django.urls import path
from .views import (
    Blogpage,
    Detailpage,
    Blogcreatepage,
    Updatepage,
    Deletepage,)

urlpatterns=[
    path('new/<int:pk>/detete',Deletepage.as_view(),name='delete'),
    path('new/<int:pk>/edit',Updatepage.as_view(), name='edit' ),
    path('new/',Blogcreatepage.as_view(),name='new'),
#    path('post/',Homepage.as_view(),name='home'),
    path('',Blogpage.as_view(),name='blog'),
    path('new/<int:pk>/',Detailpage.as_view(),name='detail'),
]