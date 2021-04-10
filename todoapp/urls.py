from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name= 'indexpage'),
    path('addtask/',addtask,name='addtask'),
    path('deletetask/<int:taskpk>/',deletetask,name='deletetask'),
    path('edittaskview/<int:taskpk>/',edittaskview),
    path('edittask/<int:taskpk>/update/',edittask)
]