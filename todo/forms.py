from django import forms
from .models import Task




class UpdateTask(forms.Form):
    class Meta:
        model = Task
        fields = ['title', ]


class CreateTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title','user' ]
        