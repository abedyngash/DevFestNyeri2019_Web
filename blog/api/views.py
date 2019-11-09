from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from blog.models import Blog
from .serializers import BlogPOSTSerializer, BlogGETSerializer

class BlogAPIListView(ListAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogGETSerializer

class BlogAPIDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogGETSerializer

class BlogAPICreateView(CreateAPIView):
	serializer_class = BlogPOSTSerializer
