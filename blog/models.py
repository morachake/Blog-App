from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    # Define the choices for the status of the post
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    # Database fields
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1
    )
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique_for_date='published')
    published = models.DateField(default=timezone.now)  # Using timezone.now without parentheses ensures the function is called at object creation
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    status = models.CharField(
        max_length=10, choices=options, default='published'
    )

    # Custom model manager for published posts
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    # Default and custom managers
    objects = models.Manager()  # The default manager.
    postobjects = PostObjects()  # Our custom manager.

    # Meta class to define ordering of posts
    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
