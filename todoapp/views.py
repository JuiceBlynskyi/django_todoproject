from django.shortcuts import render, redirect
from .services import get_item_list_content, add_new_item, delete_item


def item_list(request):
    todo_list_items_content = get_item_list_content()
    return render(request, 'todoapp/todolist.html', todo_list_items_content)


def add_todo_item(request):
    add_new_item(request)
    return redirect('home')


def delete_todo_item(request, item_id):
    delete_item(item_id)
    return redirect('home')
