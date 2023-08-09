from django.urls import path
from. import views


urlpatterns = [
    path('api/card/', views.CardAPI.as_view()),
    path('api/task/', views.TasksAPI.as_view()),
]