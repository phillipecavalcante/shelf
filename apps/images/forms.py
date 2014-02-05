from django import forms
from apps.images.models import Image
        
class ImageForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Image name'}))

    class Meta:
        model = Image
        exclude = ('description', 'url', 'gallery')