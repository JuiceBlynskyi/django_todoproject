from django.forms import ModelForm, TextInput
from ..models import TodoListItem


class ItemForm(ModelForm):
    class Meta:
        model = TodoListItem
        fields = ['content']
        widgets = {'content': TextInput()}
