from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	posted_at = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title