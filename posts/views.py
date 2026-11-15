from django.urls import reverse_lazy
from django.views import generic

from .forms import PostForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'
    ordering = ['-pub_date']  # contexto: post_list


class PostDetailView(generic.DetailView):
    # Responde automaticamente com 404 caso o post não exista
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
