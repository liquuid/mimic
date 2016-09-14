from django import forms


class SubmitText(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label="Insira seu texto aqui")


