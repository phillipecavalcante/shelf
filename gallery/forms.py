from django import forms
from gallery.models import Gallery
         
class GalleryForm(forms.ModelForm):
     
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    url = forms.URLField()
    
    class Meta:
        model = Gallery