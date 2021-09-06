from django import forms
from django.forms import widgets
from .models import Images

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = '__all__'

        widgets = {
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'image_name':forms.TextInput(attrs={'class':'form-control'}),
            'image_description':forms.Textarea(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}),
            'location':forms.SelectMultiple(attrs={'class':'form-control'}),
            'category':forms.SelectMultiple(attrs={'class':'form-control'})
        
        }
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image_name','image_description','location')

        widgets = {
            'image_name':forms.TextInput(attrs={'class':'form-control'}),
            'image_description':forms.Textarea(attrs={'class':'form-control'}),
            'location':forms.SelectMultiple(attrs={'class':'form-control'}),
            'category':forms.SelectMultiple(attrs={'class':'form-control'}),
        }
