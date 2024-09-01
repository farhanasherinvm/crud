from . import views
from django.urls import path

urlpatterns = [
    path('crud',views.crud,name='crud'),
    path('add',views.add,name='add'),
    #path('edit/<int:id>/',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
]
