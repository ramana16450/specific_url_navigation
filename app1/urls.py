from django.urls import path
from app1.views import *
app_name='venkat'
urlpatterns=[

    path('a2/',a2,name='a2'),
]