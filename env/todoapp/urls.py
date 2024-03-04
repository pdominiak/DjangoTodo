from django.urls import path
from . import views
urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markasdone/<int:pk>', views.markAsDone, name='markasdone'),
    path('markasundone/<int:pk>',views.markAsUndone, name='markasundone'),
    path('editTask/<int:pk>',views.editTask, name="edittask")
]