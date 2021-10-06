from ..models import TodoListItem
from .forms import ItemForm


def get_item_list_content():
    all_todo_items = TodoListItem.objects.all()
    content = {'all_items': all_todo_items,
               'form': ItemForm}
    return content


def add_new_item(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        # new_item = form.cleaned_data['content']
        form.save()


def delete_item(item_id):
    item = TodoListItem.objects.get(id=item_id)
    item.delete()
