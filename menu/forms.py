from django import forms
from menu.models import Menu
        
class MenuForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Menu
