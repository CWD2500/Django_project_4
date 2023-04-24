from django.shortcuts import render
from django.shortcuts import reverse

from django.views.generic import ListView , CreateView , UpdateView , DeleteView , DetailView
from .models import  EmP
from .forms import EmpForm
# Create your views here.


class Home(ListView):
    template_name = "lists.html"
    model = EmP


class Create(CreateView):
    template_name = "created.html"
    model = EmP
    form_class = EmpForm

    def get_success_url(self):
        return reverse("home")
    


class Update(UpdateView):
    template_name = "created.html"
    model = EmP
    form_class = EmpForm

    def get_success_url(self):
        return reverse("home")
    

class Details(DetailView):
    template_name = "details.html"
    model = EmP


class Delete(DeleteView):
    model =EmP
    template_name = "delete.list"

    def get_success_url(self):
        return reverse("home")





