from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import Form
from .forms import EditForm
from django.urls import reverse_lazy
#def home(request):
#	return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	#ordering = ['-id']

class ArticleView(DetailView):
	model = Post
	template_name = 'article.html'

class AddView(CreateView):
	model=Post
	form_class = Form
	template_name= 'add.html'
	#fields= '__all__'

class Edit(UpdateView):
	model=Post
	form_class=EditForm
	template_name='editpost.html'
	#fields = ['title','tag','body']

class Delete(DeleteView):
	model=Post
	template_name='delete.html'
	success_url = reverse_lazy('home')
