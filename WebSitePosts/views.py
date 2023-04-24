# from django.shortcuts import render

from django.views.generic  import ListView , DetailView  , UpdateView , CreateView , DeleteView
from .models import Post 
from django.urls import reverse  , reverse_lazy
from .forms import CRUDFORM


class PostList(ListView):
    model  =Post
    context_object_name  = 'posts'  #  templates  ارسال البيانات  لي ال
    template_name = "post/list.html"




class PostDetail(DetailView):
    model  =Post
    context_object_name  = 'posts'  #  templates  ارسال البيانات  لي ال
    template_name = "post/detail.html"


class PostCreate(CreateView):
    model  =Post
    form_class = CRUDFORM
    # context_object_name  = 'posts'  #  templates  ارسال البيانات  لي ال
    template_name = "post/create.html"
    success_url = reverse_lazy('posts')

    def form_valid(self , form):  #   يتاكد انو  تم تعبئة البيانات 
        form.instance.user = self.request.user  #  المستخدم الحالبي انا اطلبها
        return super(PostCreate , self).form_valid(form)



class PostUpdate(UpdateView):
    model  =Post
    form_class = CRUDFORM
    template_name = "post/create.html"
    success_url = reverse_lazy('posts')

    def form_valid(self , form):  #   يتاكد انو  تم تعبئة البيانات 
        return super(PostUpdate , self).form_valid(form)


    



class PostDelete(DeleteView):
    model  =Post
    # context_object_name  = 'posts'  #  templates  ارسال البيانات  لي ال
    template_name = "post/delete.html"
    def get_success_url(self):
        return reverse('posts')