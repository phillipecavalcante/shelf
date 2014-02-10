from django import forms
from apps.menu.models import Menu
        
class MenuIndexForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Menu name'}))
    
    class Meta:
        model = Menu
        exclude = ('description', 'url')
        
        
class MenuForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Menu name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Menu description'}))
    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Menu link'}))
    
    class Meta:
        model = Menu
