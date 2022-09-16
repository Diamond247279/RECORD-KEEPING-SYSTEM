from django.urls import path
from .views import *
urlpatterns = [
    path('', welcome, name='welcome'),
    path('department', homepage, name='homepage'),
    path('new-department', new_department, name='new_department'),
    path('delete/<int:id>/', delete_department, name='delete_department'),
    path('update/<int:id>/', update_department, name='update_department'),
]
