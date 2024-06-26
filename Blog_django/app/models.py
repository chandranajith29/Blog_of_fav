from django.db import models
class post(models.Model):
    photos=models.ImageField(upload_to='static/')
    title=models.CharField(max_length=300)  
    body=models.TextField() 
    created_on=models.DateTimeField(auto_now_add=True) 
    updated_on=models.DateTimeField(auto_now=True)
    categories =models.CharField(max_length=30)
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)    

# Create your models here.
