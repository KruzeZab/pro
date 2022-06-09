from django.contrib import admin

from blog.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'list_date', 'is_published']
    list_display_links = ['title', 'category']
    is_editable = ['is_published', ]


class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', ]
    

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)