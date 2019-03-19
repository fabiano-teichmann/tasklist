from django import forms
from .models import TaskList


class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ('title', 'desc', 'status')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control ', 'placeholder': 'Titulo', 'type': 'text', 'aria-label': 'Titulo'}),
            'desc': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Descrição', 'type': 'text', 'arial-label': 'Descrição'
            }),
            'status': forms.Select(attrs={'class': 'form-control ', 'placeholder': 'Status', 'type': 'select',
                                          'aria-label': 'Status'})
        }

