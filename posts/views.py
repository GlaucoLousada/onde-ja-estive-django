from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import Post


def list_posts(request):
    post_list = Post.objects.order_by('-pub_date')
    context = {'post_list': post_list}
    return render(request, 'posts/index.html', context)


def detail_post(request, pk):
    # Responde com 404 caso o post não exista
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)


def create_post(request):
    if request.method == 'POST':
        post = Post(title=request.POST['title'],
                    content=request.POST['content'],
                    pub_date=timezone.now())
        post.save()
        return HttpResponseRedirect(reverse('posts:detail', args=(post.id,)))
    return render(request, 'posts/create.html', {})


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return HttpResponseRedirect(reverse('posts:detail', args=(post.id,)))
    context = {'post': post}
    return render(request, 'posts/update.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))
    # Em requisições GET, exibe a página de confirmação
    context = {'post': post}
    return render(request, 'posts/delete.html', context)
