from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import PostForm
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
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post.id,)))
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'posts/create.html', context)


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post.id,)))
    else:
        form = PostForm(instance=post)
    context = {'post': post, 'form': form}
    return render(request, 'posts/update.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))
    # Em requisições GET, exibe a página de confirmação
    context = {'post': post}
    return render(request, 'posts/delete.html', context)
