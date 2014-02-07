from django import forms
from apps.gallery.models import Gallery
         

class GalleryForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Gallery name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Gallery description'}))
    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Gallery link'}))
    
    class Meta:
        model = Gallery



class IndexGalleryForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Gallery name'}))
    
    class Meta:
        model = Gallery
        exclude = ('description', 'url')
        
        