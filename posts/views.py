from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import CommentForm, PostForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'
    ordering = ['-pub_date']  # contexto: post_list


class PostDetailView(generic.DetailView):
    # Responde automaticamente com 404 caso o post não exista.
    # Os comentários são acessados no template por post.comments.all,
    # já ordenados pelo mais recente (Meta.ordering do modelo Comment)
    model = Post
    template_name = 'posts/detail.html'


class PostCreateView(generic.CreateView):
    # Após salvar, redireciona para Post.get_absolute_url()
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update.html'


class PostDeleteView(generic.DeleteView):
    # GET exibe a página de confirmação; POST remove o post
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:index')


def create_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # associa o comentário ao post da URL
            comment.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post.id,)))
    else:
        form = CommentForm()
    context = {'post': post, 'form': form}
    return render(request, 'posts/comment.html', context)
