from audioop import reverse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView

from theblog.models import Post
from theblog.forms import PostForm,UpdateForm

# Create your views here.
# def home(request):
#     return render(request,'home.html',{'title':"home"})
class HomeView(ListView):
    model = Post
    template_name='home.html'
    ordering=["-id"] 
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
class AddPostView(CreateView):
    model= Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields= '__all__'
class UpdatePostView(UpdateView):
    model= Post
    form_class = UpdateForm
    template_name = 'update_post.html'
    
class DeletePostView(DeleteView):
    model= Post
    template_name = 'delete_post.html'
    success_url= reverse_lazy('home')
    