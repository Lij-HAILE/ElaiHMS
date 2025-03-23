from django.urls import path
from .views import (create_question,create_answer,delete_answer,
                    delete_question,create_order,edit_time,
                    MyDashboard,delete_order,create_table,delete_table
                    )
urlpatterns = [
    path('dashboard/',MyDashboard.as_view(),name='dashboard'),
    path('create-question',create_question,name="create-question"),
    path('create-answer',create_answer,name="create-answer"),
    path('create-order',create_order,name="create-order"),
    path('delete-answer/<int:id>',delete_answer,name="delete-answer"),
    path('delete-question/<int:id>',delete_question,name="delete-question"),
    path('edit-time/',edit_time,name="edit-time"),
    path('delete-order/<int:id>',delete_order,name="delete-order"),
    path('create-table/',create_table,name='create-table'),
    path('delete-table/<int:id>',delete_table,name="delete-table"),


]