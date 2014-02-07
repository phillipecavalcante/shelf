from django import forms
from apps.images.models import Image
        
class IndexImageForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Image name'}))
    
    class Meta:
        model = Image
        exclude = ('description', 'url')
    
class ImageForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Image name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Image description'}))
    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Image link'}))
    
    class Meta:
        model = Image
        