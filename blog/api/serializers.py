from rest_framework import serializers 
from django.contrib.auth.models import User
from blog.models import Blog


class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ('id', 'username', 'email')

class BlogPOSTSerializer(serializers.ModelSerializer):
	
	author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
	class Meta:
		model = Blog
		fields = ('id', 'title', 'body', 'author', 'posted_at')

class BlogGETSerializer(serializers.ModelSerializer):
	author = UserSerializer()
	
	class Meta:
		model = Blog
		fields = ('id', 'title', 'body', 'author', 'posted_at')