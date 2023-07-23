from django.shortcuts import render
from django.views.generic import ListView,DetailView
from  .models import Posts, Blog
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

#class Homepage(ListView):
#    model = Posts
#    template_name = 'home.html'

class Blogpage(ListView):
    model = Blog
    template_name = 'blog.html'

class Detailpage(DetailView):
    model = Blog
    template_name = 'detail.html'

class Blogcreatepage(CreateView):
    model = Blog
    template_name = 'new_det.html'
    fields = ['title','author','izoh']

class Updatepage(UpdateView):
    model = Blog
    template_name = 'update.html'
    fields = ['title','izoh']

class Deletepage(DeleteView):
    model=Blog
    template_name = 'delete.html'
    success_url = reverse_lazy('blog')
