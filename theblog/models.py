from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=20,default="null")
    author=models.ForeignKey(User,default=0,on_delete=models.CASCADE)
    body=models.TextField(default="nul")
    post_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
