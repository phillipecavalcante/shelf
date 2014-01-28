from django import forms
from pages.models import Page
from menu.models import Menu
        
class PageForm(forms.ModelForm):
    
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':80,
                                                            'rows':10}))

    class Meta:
        model = Page