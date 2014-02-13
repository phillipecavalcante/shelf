#===============================================================================
# DJANGO
#===============================================================================
from django import forms
from django.utils.translation import ugettext as _
#===============================================================================
# APPS
#===============================================================================
from apps.images.models import Image

#===============================================================================
# INDEXES        
#===============================================================================

class ImageIndexForm(forms.ModelForm):
    
    class Meta:
        model = Image
        exclude = ('description', 'url',)
    
    def __init__(self, *args, **kwargs):
        super(ImageIndexForm, self).__init__(*args, **kwargs)
        
        #=======================================================================
        # LABELS
        #=======================================================================
        self.fields['name'].label = _('Image name')
        self.fields['public'].label = _('Published')
        #=======================================================================
        # WIDGETS
        #=======================================================================
       
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['gallery'].widget.attrs['class'] = 'form-control'
         
        self.fields['name'].widget.attrs['placeholder'] = 'Example'        
    

    
class ImageForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['gallery'].widget.attrs['class'] = 'form-control'
        
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Image name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Image description'}))
    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Image link'}))
    
    class Meta:
        model = Image
