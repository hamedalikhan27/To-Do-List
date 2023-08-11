from django.urls import path
from . import views

urlpatterns = [
    path('',views.tasks_views, name='list'),
    path('/update/<str:pk>/',views.update,name='update'),
    path('/delete/<str:pk>/',views.delete,name='delete')
    
]