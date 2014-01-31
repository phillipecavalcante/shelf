from django import forms
from apps.gallery.models import Gallery, Image
         
class GalleryForm(forms.ModelForm):
     
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    url = forms.URLField(required=False)
    
    class Meta:
        model = Gallery
        
        
class ImageForm(forms.ModelForm):
     
    class Meta:
        model = Image