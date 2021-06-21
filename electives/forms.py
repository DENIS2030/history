from django import forms
from lessons.models import  Gallery



class GalleryForm(forms.ModelForm):

    class Meta:
        model =  Gallery
        fields = ['elective','image','user']