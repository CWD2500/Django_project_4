from django import forms
from .models import Employees


class EmployeesForm(forms.Form):

# attrs    css اضاغة ال 
    name = forms.CharField(widget   =   forms.TextInput(attrs={"class":"form-control" , "placeholder":"name"}))
    age  = forms.IntegerField(widget= forms.TextInput (attrs={"class":"form-control" , "placeholder":"Age"}))
    level = forms.CharField(widget  =   forms.Textarea (attrs={"class":"form-control" , "placeholder":"Level"}))

#  form  :    بحددللك   مع انو  كلاس  رح ترتبط 

# class Meta :    تبعك شو  اضافة فينك تحدد الحقول  models   غكرتها انو  تحدد  ال

    class Meta:
        model = Employees
        fields = ["name" , "age" , "level" ]