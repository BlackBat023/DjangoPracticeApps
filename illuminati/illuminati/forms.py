from django import forms
from .models import Messages

class MsgForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Enter your ideas here...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Messages
        exclude = ("user", )