from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField('título', max_length=255)
    # O conteúdo é armazenado como HTML e renderizado com o filtro |safe
    content = models.TextField('conteúdo')
    pub_date = models.DateTimeField('data de postagem', default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.id,))


class Comment(models.Model):
    # O autor referencia o modelo User configurado no projeto
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               verbose_name='autor')
    text = models.TextField('texto')
    pub_date = models.DateTimeField('data de postagem', default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')

    class Meta:
        ordering = ['-pub_date']  # mais recente primeiro

    def __str__(self):
        return f'{self.author.username}: {self.text[:40]}'
