from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from .models import Blog
from .forms import BlogForm, CustomAuthenticationForm, CustomUserCreationForm
from .filters import BlogFilter
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from modal_test.utils import render_to_pdf
import datetime
# Create your views here.

class BlogListView(ListView):
	model = Blog		
	template_name = 'blog/blog_list.html'

	def get_context_data(self, **kwargs):
	    context = super(BlogListView, self).get_context_data(**kwargs)
	    blog_list = Blog.objects.all()
	    blog_filter = BlogFilter(self.request.GET, queryset=blog_list)
	    context['filter'] = blog_filter
	    return context



class BlogCreateView(BSModalCreateView):
	template_name = 'blog/blog_form.html'
	form_class = BlogForm
	success_message = 'Success: Blog created.'
	success_url = reverse_lazy('home')

	def get_context_data(self, **kwargs):
	    context = super(BlogCreateView, self).get_context_data(**kwargs)
	    context['title'] = 'Create Blog'
	    return context

class BlogUpdateView(BSModalUpdateView):
	model = Blog
	
	form_class = BlogForm
	success_message = 'Success: Blog Updated.'
	success_url = reverse_lazy('home')

class BlogDetailView(BSModalReadView):
    model = Blog

class BlogDeleteView(BSModalDeleteView):
    model = Blog
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('home')

class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('home')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'blog/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('home')

def search(request):
    blog_list = Blog.objects.all()
    blog_filter = BlogFilter(request.GET, queryset=blog_list)
    return render(request, 'blog/blog_list.html', {'filter': blog_filter})

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
    	blogs = Blog.objects.filter(author=self.request.user)
    	
    	data = {}
    	for blog in blogs:
    	 	data['blog'] = blog
    	pdf = render_to_pdf('pdf_output.html', data)
    	return HttpResponse(pdf, content_type='application/pdf')

# data = {
# 		    'blog': blog,
# 		}

# 		pdf = render_to_pdf('pdf_output.html', data)
# 		return HttpResponse(pdf, content_type='application/pdf')