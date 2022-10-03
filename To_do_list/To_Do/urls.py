from django.urls import path
from . import views

app_name = "To_Do"
urlpatterns = [
    path('',views.index, name="index"),
    path('To_Do/add_task/', views.add_task, name="add_task"),

]
