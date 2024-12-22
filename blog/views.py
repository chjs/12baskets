from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    post_list = Post.objects.filter(category=category).order_by('-pk')
    category_list = Category.objects.all()

    return render(request, 'blog/post_list.html', {'category': category, 'categories': category_list, 'post_list': post_list})

class PostDetail(DetailView):
    model = Post
