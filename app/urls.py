from django.urls import path
from app.views import *
app_name='ramana'
urlpatterns=[

    path('a1/',a1,name='a1'),
]