from django.urls import path
from .views import BlogListView, BlogUpdateView, BlogCreateView, BlogDetailView, BlogDeleteView, SignUpView, search, GeneratePdf

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('blogs/add/', BlogCreateView.as_view(), name='blog-create'),
    path('blogs/<int:pk>/update', BlogUpdateView.as_view(), name='blog-update'),
    path('blogs/<int:pk>/delete', BlogDeleteView.as_view(), name='blog-delete'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('search/', search, name='search'),
    path('pdf/', GeneratePdf.as_view(), name='generate-pdf')
]
