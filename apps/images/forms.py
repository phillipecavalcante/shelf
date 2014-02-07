from django import forms
from apps.images.models import Image
        
class ImageForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Image name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Image description'}))
    
    class Meta:
        model = Image