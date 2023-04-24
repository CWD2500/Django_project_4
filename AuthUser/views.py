from django.shortcuts import render , redirect
from django.views.generic import TemplateView , FormView
from django.contrib.auth.views import LoginView  , LogoutView   
from django.urls  import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth import login


# Create your views here.
# FormView: forms يلي موجود بي  form  حتى تنادي ال 
# LoginRequiredMixin :    login   للحمياة من الصفحة اذا هوي ما عامل 

class HomeView( LoginRequiredMixin , TemplateView):
    template_name = "user/home.html"


class ProFileView(LoginRequiredMixin, TemplateView):
    template_name= "user/proFile.html"


class MyLoginView(LoginView):
    #  اذا كان المستخدم اصلن عامل تسجيل فا ما حجة انو مرة تانية تعمب تسجيل 
    redirect_authenticated_user = True
    # template_name= "user/proFile.html"  

    def get_success_url(self):
        messages.info(self.request , "Welcome in Your ProFile ")
        return reverse_lazy('proFile')
    
    #   اذا ماكتب اسم وكلمة المرور  غلط  رح يشتغل هاد ال دالة 
    def form_invalid(self, form):
        messages.error(self.request , "Error username or password")
        return self.render_to_response(self.get_context_data(form=form))
    

class RegisterView(FormView):
    redirect_authenticated_user = True
    template_name = "registration/register.html"
    form_class = RegistrationForm
   
    success_url = reverse_lazy('proFile')

# dispatch  يتحقق من اذا المستخدم مسحل ةلا ةلاء 
    def dispatch(self , request , *args ,  **kwargs):
        if request.user.is_authenticated:
            return redirect('proFile')

        super(RegisterView , self).dispatch(request , *args ,  **kwargs)
         
    def form_valid(self,form):
        user=form.save()
        if  user:
            login(self.request , user)  #  مع طلب البيانات  login بعد االمستخدم يسجلل الدخول  رح يحول  الى 
        return super(RegisterView , self).form_valid(form)

    
        



