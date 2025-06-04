from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag

class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['tags'] = Tag.objects.all().order_by('name')

        page = context['page_obj']
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(page.number, on_each_side=2, on_ends=0)
        context['pagelist'] = pagelist
        return context


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    post_list = Post.objects.filter(category=category).order_by('-pk')
    category_list = Category.objects.all()
    tag_list = Tag.objects.all().order_by('name')

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'category': category,
            'categories': category_list,
            'tags': tag_list,
        }
    )


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()
    category_list = Category.objects.all()
    tag_list = Tag.objects.all().order_by('name')

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'tag': tag,
            'categories': category_list,
            'tags': tag_list,
        }
    )


class PostDetail(DetailView):
    model = Post
