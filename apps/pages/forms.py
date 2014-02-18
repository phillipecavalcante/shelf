from django import forms
from django.utils.translation import ugettext as _

from apps.pages.models import *


class PageIndexForm(forms.ModelForm):
    
    class Meta:
        model = Page
        exclude = ('public', 'url', 'description','content', 'gallery')
    
    def __init__(self, *args, **kwargs):
        super(PageIndexForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].label = _('Page name')
        self.fields['name'].help_text = 'It is not the page title.'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Example page'
        

        self.fields['menu'].label = _('Append to')
        self.fields['menu'].help_text = 'Append to this page a menu.'
        self.fields['menu'].widget.attrs['class'] = 'form-control'
        
class PageForm(forms.ModelForm):
    
    class Meta:
        model = Page
    
    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        
            
        #=======================================================================
        # REQUIRED
        #=======================================================================
        
        self.fields['url'].required = True
        
        #=======================================================================
        # LABELS
        #=======================================================================
        self.fields['name'].label = _('Link page name')
        self.fields['description'].label = _('Description')
        self.fields['url'].label = _('Redirects to')
        self.fields['public'].label = _('Published')
        self.fields['menu'].label = _('Appended to')
        #=======================================================================
        # WIDGETS
        #=======================================================================
       
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['url'].widget.attrs['class'] = 'form-control'
        self.fields['menu'].widget.attrs['class'] = 'form-control'
         
        self.fields['name'].widget.attrs['placeholder'] = 'Example'
        self.fields['description'].widget.attrs['placeholder'] = 'Page Description'
        self.fields['url'].widget.attrs['placeholder'] = 'www.example.com'
        
                
# class TextPageIndexForm(forms.ModelForm):
#  
#     class Meta:
#         model = TextPage
#         exclude = ('description', 'url', 'public', 'content')
#            
#     def __init__(self, *args, **kwargs):
#         super(TextPageIndexForm, self).__init__(*args, **kwargs)
#         
#         #=======================================================================
#         # LABELS
#         #=======================================================================
#         self.fields['name'].label = _('Text page name')
#         self.fields['menu'].label = _('Appended to')
#         #=======================================================================
#         # WIDGETS
#         #=======================================================================
#        
#         self.fields['name'].widget.attrs['class'] = 'form-control'
#         self.fields['menu'].widget.attrs['class'] = 'form-control'
#         self.fields['name'].widget.attrs['placeholder'] = 'Example'
#         
# class TextPageForm(forms.ModelForm):
#     
#     class Meta:
#         model = TextPage
#     
#     def __init__(self, *args, **kwargs):
#         super(TextPageForm, self).__init__(*args, **kwargs)
#         
#         
#         #=======================================================================
#         # LABELS
#         #=======================================================================
#         self.fields['name'].label = _('Link page name')
#         self.fields['description'].label = _('Description')
#         self.fields['url'].label = _('Redirects to')
#         self.fields['public'].label = _('Published')
#         self.fields['menu'].label = _('Appended to')
#         #=======================================================================
#         # WIDGETS
#         #=======================================================================
#        
#         self.fields['name'].widget.attrs['class'] = 'form-control'
#         self.fields['description'].widget.attrs['class'] = 'form-control'
#         self.fields['url'].widget.attrs['class'] = 'form-control'
#         self.fields['menu'].widget.attrs['class'] = 'form-control'
#          
#         self.fields['name'].widget.attrs['placeholder'] = 'Example'
#         self.fields['description'].widget.attrs['placeholder'] = 'Page Description'
#         self.fields['url'].widget.attrs['placeholder'] = 'www.example.com'
# 
# class GalleryPageForm(forms.ModelForm):
#     
#     class Meta:
#         model = GalleryPage
#     
#     def __init__(self, *args, **kwargs):
#         super(GalleryPageForm, self).__init__(*args, **kwargs)
#         
#             
#         #=======================================================================
#         # REQUIRED
#         #=======================================================================
#         
#         self.fields['url'].required = True
#         
#         #=======================================================================
#         # LABELS
#         #=======================================================================
#         self.fields['name'].label = _('Link page name')
#         self.fields['description'].label = _('Description')
#         self.fields['url'].label = _('Redirects to')
#         self.fields['public'].label = _('Published')
#         self.fields['menu'].label = _('Appended to')
#         #=======================================================================
#         # WIDGETS
#         #=======================================================================
#        
#         self.fields['name'].widget.attrs['class'] = 'form-control'
#         self.fields['description'].widget.attrs['class'] = 'form-control'
#         self.fields['url'].widget.attrs['class'] = 'form-control'
#         self.fields['menu'].widget.attrs['class'] = 'form-control'
#          
#         self.fields['name'].widget.attrs['placeholder'] = 'Example'
#         self.fields['description'].widget.attrs['placeholder'] = 'Page Description'
#         self.fields['url'].widget.attrs['placeholder'] = 'www.example.com'
#         
#         
#         
# class ProductPageForm(forms.ModelForm):
#     
#     class Meta:
#         model = ProductPage
#     
#     def __init__(self, *args, **kwargs):
#         super(ProductPageForm, self).__init__(*args, **kwargs)
#         
#             
#         #=======================================================================
#         # REQUIRED
#         #=======================================================================
#         
#         self.fields['url'].required = True
#         
#         #=======================================================================
#         # LABELS
#         #=======================================================================
#         self.fields['name'].label = _('Link page name')
#         self.fields['description'].label = _('Description')
#         self.fields['url'].label = _('Redirects to')
#         self.fields['public'].label = _('Published')
#         self.fields['menu'].label = _('Appended to')
#         #=======================================================================
#         # WIDGETS
#         #=======================================================================
#        
#         self.fields['name'].widget.attrs['class'] = 'form-control'
#         self.fields['description'].widget.attrs['class'] = 'form-control'
#         self.fields['url'].widget.attrs['class'] = 'form-control'
#         self.fields['menu'].widget.attrs['class'] = 'form-control'
#          
#         self.fields['name'].widget.attrs['placeholder'] = 'Example'
#         self.fields['description'].widget.attrs['placeholder'] = 'Page Description'
#         self.fields['url'].widget.attrs['placeholder'] = 'www.example.com'
#         
# class GalleryPageIndexForm(forms.ModelForm):
#     
#     def __init__(self, *args, **kwargs):
#         super(GalleryPageIndexForm, self).__init__(*args, **kwargs)
#         self.fields['menu'].widget.attrs['class'] = 'form-control'
#         self.fields['gallery'].widget.attrs['class'] = 'form-control'
#         
#     
#     name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Example'}))
# 
#     
#     class Meta:
#         model = GalleryPage
#         exclude = ('description', 'url')
#         
# class ProductPageIndexForm(forms.ModelForm):
#     
#     def __init__(self, *args, **kwargs):
#         super(ProductPageIndexForm, self).__init__(*args, **kwargs)
#         self.fields['menu'].widget.attrs['class'] = 'form-control'
#         
#     name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Example'}))
#     
#     class Meta:
#         model = ProductPage
#         exclude = ('description', 'url',)
#         