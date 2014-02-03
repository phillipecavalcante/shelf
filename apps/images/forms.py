from django import forms
from apps.images.models import Image
        
class ImageForm(forms.ModelForm):
    
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'type':'url'}))
    gallery = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = Image