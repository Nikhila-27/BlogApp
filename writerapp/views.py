from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView
from django.contrib.auth.models import User
from writerapp.forms import UserLoginForm,UserRegisterForm,WriterBlogForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from writerapp.models import BlogModel
from django.views import View


# Create your views here.
class WriterHome(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['bloglist']=BlogModel.objects.filter(user=self.request.user)
        return context

class UserRegisterView(CreateView):
    model=User
    form_class=UserRegisterForm
    template_name="user_register.html"

    def post(self,request,*args,**kwargs):
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"Register Successful")
            return redirect('writer_home')
        else:
            messages.warning(request,"Invalid")
            return redirect('user_register')
        

class UserLoginView(FormView):
    form_class=UserLoginForm
    template_name='user_login.html'

    def post(self,request,*args,**kwargs):
        username=request.POST.get("username")
        password=request.POST.get("password")
        usertype=request.POST.get("usertype")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if usertype=="writer":
                messages.success(request,'Login Successful')
                return redirect('writer_home')
            else:
                messages.success(request,'Login Successful')
                return redirect('reader_home')
            

class BlogCreateView(CreateView):
    model=BlogModel
    form_class=WriterBlogForm
    template_name="blog_create.html"

    def post(self,request,*args,**kwargs):
        form=WriterBlogForm(request.POST,request.FILES)
        if form.is_valid():
            BlogModel.objects.create(**form.cleaned_data,user=request.user)
            return redirect('writer_home')
        


class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("user_login")


           
        
