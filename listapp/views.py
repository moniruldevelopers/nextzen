from django.shortcuts import render
from .models import Category, Post_list

# Create your views here.
def home(request):
    categories_with_content = Category.objects.filter(post_list__isnull=False).distinct()
    post_lists = Post_list.objects.filter(category__in=categories_with_content)
    return render(request, 'index.html', {'categories_with_content': categories_with_content, 'post_lists': post_lists})