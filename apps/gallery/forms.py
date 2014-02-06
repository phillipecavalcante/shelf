from django import forms
from apps.gallery.models import Gallery
from apps.images.models import Image
         
class GalleryForm(forms.ModelForm):
     
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'type':'url'}))
    
    class Meta:
        model = Gallery
        
        