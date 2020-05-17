from django.urls import path
from . import views

app_name = 'tasty'
urlpatterns = [
    # /tasty/
    path('', views.index)
]
