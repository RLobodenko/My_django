from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    telefone = forms.CharField(label="Телефон")
    comment = forms.CharField(label="Комментарий")