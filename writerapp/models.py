from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to="media")
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class CommentModel(models.Model):
    comment=models.TextField(max_length=100)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(BlogModel,on_delete=models.CASCADE)