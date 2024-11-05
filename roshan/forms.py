from django import forms

from . models import Dataset,Data,Tags,Information


class DatasetForms(forms.ModelForm):
    class Meta:
        model=Dataset
        # fields="__all__"
        exclude=['is_active']
        

class DataForms(forms.ModelForm):
    class Meta:
        model=Data
        # fields="__all__"
        exclude=['is_active']

class TagsForms(forms.ModelForm):
    class Meta:
        model=Tags
        # fields="__all__"
        exclude=['is_active']
        
class InformationForms(forms.ModelForm):
    class Meta:
        model=Information
        # fields="__all__"
        exclude=['is_active']
        
