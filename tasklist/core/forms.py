from django import forms
from .models import TaskList


class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ('title', 'status', 'desc')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control ', 'placeholder': 'Titulo', 'type': 'text', 'aria-label': 'Titulo'}),
            'status': forms.Select(attrs={'class': 'form-control ', 'placeholder': 'Status', 'type': 'select',
                                          'aria-label': 'Status'}),
            'desc': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Descrição', 'type': 'text', 'arial-label': 'Descrição'
            })

        }

