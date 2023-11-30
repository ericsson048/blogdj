from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='titre')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_on = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name='publie')
    content = models.TextField(blank=True, verbose_name='contenu')
    image= models.ImageField(blank=True,null=True, upload_to='blog')

    class Meta:
        ordering = ['-create_on']
        verbose_name = 'article'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    @property
    def author_default(self):
        return self.author.username if self.author else "l'auteur inconnue"

    def get_absolute_url(self):
        return reverse('posts:home')
