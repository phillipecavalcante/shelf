from django import forms
from apps.menu.models import Menu
        
class MenuIndexForm(forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        super(MenuIndexForm, self).__init__(*args, **kwargs)
        self.fields['parent'].widget.attrs['class'] = 'form-control'
        
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Menu name'}))
    
    class Meta:
        model = Menu
        exclude = ('description', 'url')
        
        
class MenuForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['parent'].widget.attrs['class'] = 'form-control'
        
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Menu name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Menu description'}))
    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Menu link'}))
    
    class Meta:
        model = Menu
