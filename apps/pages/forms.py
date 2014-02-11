from django import forms
from apps.pages.models import LinkPage, TextPage, GalleryPage, ProductPage
from apps.menu.models import Menu
from apps.gallery.models import Gallery

class LinkPageIndexForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Example'}))
    url = forms.URLField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'www.example.com'}), label='Redirect to')
    
    
    class Meta:
        model = LinkPage
        exclude = ('description',)
        
        
class TextPageIndexForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Example'}))
    
    class Meta:
        model = TextPage
        exclude = ('description', 'url', 'public', 'content')

class GalleryPageIndexForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(GalleryPageIndexForm, self).__init__(*args, **kwargs)
        self.fields['menu'].widget.attrs['class'] = 'form-control'
        self.fields['gallery'].widget.attrs['class'] = 'form-control'
        
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Example'}))

    
    class Meta:
        model = GalleryPage
        exclude = ('description', 'url')
        
class ProductPageIndexForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Example'}))
    
    class Meta:
        model = ProductPage
        exclude = ('description', 'url',)
        