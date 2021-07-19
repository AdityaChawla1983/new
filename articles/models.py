from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
class Article(models.Model):
    title = models.CharField(max_length=255)
    #designation = models.CharField(max_length=20, null=False, blank=False)
    mainphoto = models.ImageField(upload_to='pictures/%Y/%M/%D/',  null=True, blank = True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,
)
def __str__(self):
    return self.title + '|' + str(self.author) 
def get_absolute_url(self):
   return reverse('article_detail', args=[str(self.id)])
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
    related_name='comments'
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('article_list')
    
    #car = Article.objects.get(name ="Aditya Devloper")
    #car.mainphoto
    #car.mainphoto.path
    #car.mainphoto.url