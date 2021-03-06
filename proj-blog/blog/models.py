from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.urls import reverse
from datetime import datetime

from .utils import generate_unique_slug

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=55)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=160)
    photo_main = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    content = RichTextUploadingField()
    views = models.IntegerField(default=0)
    list_date = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-list_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_unique_slug(Blog, self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'category':self.category, 'slug':self.slug})
