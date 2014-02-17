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
        # REQUIRED
        #=======================================================================
                
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

    class Meta:
        model = Image
          
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        
        #=======================================================================
        # REQUIRED
        #=======================================================================
        
        self.fields['description'].required = False
        
        
        self.fields['name'].label = _('Image name')
        self.fields['public'].label = _('Published')
        
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['url'].widget.attrs['class'] = 'form-control'
        self.fields['gallery'].widget.attrs['class'] = 'form-control'
        
        
        self.fields['name'].widget.attrs['placeholder'] = 'Exemplo'
        self.fields['url'].widget.attrs['placeholder'] = 'Image link'
             

