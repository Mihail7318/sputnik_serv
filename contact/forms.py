from django import forms


class AboutForm(forms.Form):
    name = forms.CharField(label="Ваше имя")
    email = forms.EmailField()
    text = forms.CharField(label="Сообщение", widget=forms.Textarea)