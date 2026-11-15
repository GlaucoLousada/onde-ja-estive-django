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
