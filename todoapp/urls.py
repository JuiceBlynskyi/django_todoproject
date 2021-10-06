from django.urls import path
from .views import item_list, add_todo_item, delete_todo_item


urlpatterns = [
    path('todoapp/', item_list, name='home'),
    path('todoapp/add_item', add_todo_item, name='add_item'),
    path('todoapp/delete_item/<int:item_id>/', delete_todo_item, name='delete_item'),
]
