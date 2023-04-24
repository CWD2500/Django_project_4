from  django import forms
from .models  import EmP


class EmpForm(forms.ModelForm):
    name = forms.CharField(widget   =   forms.TextInput(attrs={"class":"form-control" , "placeholder":"name"}))
    age  = forms.IntegerField(widget= forms.TextInput (attrs={"class":"form-control" , "placeholder":"Age"}))
    level = forms.CharField(widget  =   forms.Textarea (attrs={"class":"form-control" , "placeholder":"Level"}))


    class Meta:
        model = EmP
        fields = ["name" , "age" , "level"]


