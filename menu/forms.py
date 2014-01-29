from django import forms
from menu.models import Menu
        
class MenuForm(forms.ModelForm):
    #parent
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    position = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    #public
    
    class Meta:
        model = Menu
