from django import forms

from .models import STATUS_CHOICES


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.Form):
    title = forms.CharField(
        max_length=128,
        required=True,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    description = forms.CharField(
        max_length=128,
        required=True,
        label='Описание',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    full_description = forms.CharField(
        max_length=4096,
        required=False,
        label='Полное описание',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    deadline = forms.DateField(
        required=True,
        widget=DateInput(attrs={'class': 'form-control'})
    )


