from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель для Группы"""

    title = models.CharField(
        max_length=200,
        help_text='Название группы'
    )
    slug = models.SlugField(
        unique=True,
        help_text='URL группы'
    )
    description = models.TextField(help_text='Описание группы')

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель для Поста"""
    text = models.TextField(help_text='Текст публикации')
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True, blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель для Комментариев"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True
    )


class Follow(models.Model):
    """Модель для Подписчиков"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_following'
            )
        ]
