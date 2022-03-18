from app2.views import a2_kgf
from django.urls import path
app_name='app2'
urlpatterns=[
    path('a2_kgf/',a2_kgf,name='a2_kgf'),
]