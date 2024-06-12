from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name="kitab_name")
    content = RichTextField(verbose_name="subject")
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='Article Images', null=True, blank=True, verbose_name="Sekil")
    # image = models.ImageField(upload_to="myIMG", null=True, blank=True, )
    def __str__(self):
        return f"{self.title} | {self.author}"


class Comment(models.Model):
    article =  models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Meqale", related_name="comments")
    comment_author = models.CharField(max_length=150, verbose_name="ad")
    comment_content = models.TextField(verbose_name="Şerh")
    comment_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.comment_author} "