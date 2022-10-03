from django.urls import path
from . import views

app_name = "To_Do"
urlpatterns = [
    path('',views.index, name="index")
]
