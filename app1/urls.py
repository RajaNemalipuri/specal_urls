from app1.views import a1_RRR
from django.urls import path
app_name='app1'
urlpatterns=[
    path('a1_RRR/',a1_RRR,name='a1_RRR'),
]