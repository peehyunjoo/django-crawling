from django import forms
from .models import join, choice
class JoinForm(forms.ModelForm):
    class Meta:
        model = join
        fields = ('email', 'id', 'nickname', 'password')

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = choice
        fields = ('id', 'etc1', 'etc2')