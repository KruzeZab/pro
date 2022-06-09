from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.models import Blog

class IndexView(ListView):
    context_object_name = 'blogs'
    template_name = 'blog/index.html'
    paginate_by = 12

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).only('title', 'category', 'photo_main', 'list_date', 'description', 'slug')


class BlogView(DetailView):
    template_name = 'blog/article.html'
    model = Blog
    context_object_name = 'article'



class SearchView(ListView):
    context_object_name = 'blogs'
    template_name = 'blog/search.html'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Blog.objects.filter(is_published=True).filter(title__icontains=query).only('title', 'category', 'photo_main', 'list_date', 'description', 'slug')
