from django.db import models

class Author(models.Model):

    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, primary_key=True)

class Post(models.Model):

    POST_TYPES = [('c', 'copyright'), ('p', 'public content')]

    title = models.CharField(max_length=200)
    content = models.TextField()
    post_type = models.CharField(max_length=1, choices=POST_TYPES)
    image = models.ImageField(upload_to='uploads')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

