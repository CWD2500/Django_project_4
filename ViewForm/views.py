from django.shortcuts import render
from .models import Employees
from .forms import EmployeesForm
from django.views.generic import ListView  , CreateView , UpdateView , DeleteView , DetailView
# Create your views here.

#  reverse_lazy       attrbute  يستخدم مع ال 
# revers     function   يستخدم مع ال 
from django.shortcuts import  reverse


class Home(ListView):
    model = Employees
    template_name = "list.html"





class Create(CreateView):
    model = Employees
    template_name = "create.html"
    # Select Form  the Connected Model DataBase
    form_class = EmployeesForm
    def get_success_url(self):
        return reverse("home")
    

class Details(DetailView):
    model = Employees
    template_name = "detail.html"

class Update(UpdateView):
    model = Employees
    template_name = "create.html"
    form_class = EmployeesForm

    def get_success_url(self):
        return reverse("home")


class Delete(DeleteView):
    model =Employees
    template_name = "delete.list"

    def get_success_url(self):
        return reverse("home")




