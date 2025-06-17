from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from writerapp.models import BlogModel,CommentModel
from readerapp.forms import AddCommentForm
from django.contrib import messages

# Create your views here.

class ReaderHome(ListView):
    template_name="reader_home.html"
    model=BlogModel
    context_object_name="bloglist"


class ReaderBlogDetail(DetailView):
    model=BlogModel
    template_name="reader_detail.html"
    context_object_name="blogdetail"
    pk_url_kwarg="id"



class AddCommentView(CreateView):
    model=CommentModel
    form_class=AddCommentForm
    template_name="add_comment.html"

    def post(self,request,*args,**kwargs):
        print(kwargs)
        form=AddCommentForm(request.POST,request.FILES)
        blog=BlogModel.objects.get(id=kwargs.get("id"))
        print(kwargs)
        if form.is_valid():
            CommentModel.objects.create(**form.cleaned_data,user=request.user,blog=blog)
            # messages.success(request,"comment added")
            # return redirect('reader_home')
            return redirect('reader_detail',id=kwargs.get("id"))

class ListCommentView(TemplateView):
    template_name='list_comment.html'
    model=CommentModel
    

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        blog=BlogModel.objects.get(id=kwargs.get("id"))
        context['commentlist']=CommentModel.objects.filter(blog=blog)
        # context['commentlist']=blog.commentmodel_set.all()
        return context




