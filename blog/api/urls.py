from django.urls import path
from .views import BlogAPIListView, BlogAPIDetailView, BlogAPICreateView
urlpatterns = [
	path('', BlogAPIListView.as_view(), name='blog-api-list'),
	path('create/', BlogAPICreateView.as_view(), name='blog-api-create'),
	path('<int:pk>/', BlogAPIDetailView.as_view(), name='blog-api-detail')
]