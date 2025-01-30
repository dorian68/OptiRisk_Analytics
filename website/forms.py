from django import forms
from .models import UploadedFile

class UploadedFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ["file"]

class RiskSimlatorfielsForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        columns = kwargs.pop('colums',[])
        super().__init__(*args,**kwargs)
        for col in columns:
            self.fields[col] = forms.ChoiceField(choises=[(col,col) for col in columns])