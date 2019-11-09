from .models import Blog
import django_filters

class BlogFilter(django_filters.FilterSet):
	# title = django_filters.CharFilter(lookup_expr='icontains')
	def __init__(self, *args, **kwargs):
	    super(BlogFilter, self).__init__(*args, **kwargs)
	    self.filters['author'].label="Select Author"
	class Meta:
		model = Blog
		fields = [ 'author']

		labels={
		'author': 'Select Author'
		}