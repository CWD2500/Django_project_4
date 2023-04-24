from django.shortcuts import render
from django.views.generic import TemplateView , CreateView , ListView , DetailView , UpdateView , DeleteView 
# ListView  اظهار البيانات 
from django.urls import reverse_lazy
from .models import Patient


# Create your views here.

# def home (request):
#     return render(request , 'home.html')


class Home(TemplateView):
    template_name = "home.html"


class ThankYouPage(TemplateView):
    template_name ="thankyou.html"


class CreatePatient(CreateView):
   
#    template_name
#  Patient_form.html   تلقائي رح ياهود اسم الصفحة بشرط انو يكون بهاد الشكل class في حالة ما سمية اسم ال الصفحة الانشاء  ال 
   model = Patient
# model :  Models  تحديد اسم ال 
#    fields =['firstName' , 'lastName']
   fields ='__all__'
# fields :   تحديد بعض البيانات للملاء 
   success_url = reverse_lazy('classViews:thank')
# success_url :   توجيه المستخدم لصفة اخرة بعد ملاء البيانات 
# reversed_lazy  : اعادة التوجيه الى صفحة اخرى 



class PatientListView(ListView):
    # template_name="patient_list.html"
    # patient_list.html
    model = Patient
    queryset = Patient.objects.order_by('firstName')
   #  queryset  models القكرة انو  اضيف معلومات اضافية في ال 
    context_object_name ="patient_lists"
    # context_object_name  : for تبع ال html  لقول اعطيني المتغير يلي بدو يروح على صفخة ال 


class PatientDetailView(DetailView):
   model = Patient


class PatientUpdateView(UpdateView):
    model = Patient
    fields= "__all__"   
    success_url = reverse_lazy('classViews:thank')


class PatientDeleteView(DeleteView):
   # template_name = "patient_confirm_delete"
   # confirm : للتأكيد على الحزف
   model = Patient
   success_url = reverse_lazy('classViews:patientListViews')

