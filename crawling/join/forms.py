from django import forms
from .models import join
class JoinForm(forms.ModelForm):
    class Meta:
        model = join
        fields = ('email', 'id', 'nickname', 'password')