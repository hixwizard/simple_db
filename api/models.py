from django.db import models
from django.contrib.auth.models import AbstractUser

from core.constants import ROLE_CHOICES, ROLE_CHOICES_LIST, MAX_TITLE


class User(AbstractUser):
    """
    Модель пользователя. Роли: администратор, модератор, пользователь.
    """
    username = models.CharField(
        max_length=MAX_TITLE,
        unique=True, verbose_name='Имя', help_text='Имя пользователя.')
    email = models.EmailField(
        verbose_name='Электронная почта', help_text='Электронная почта.')
    password = models.CharField(
        max_length=MAX_TITLE, verbose_name='Пароль', help_text='Пароль.')
    avatar = models.ImageField(
        upload_to='avatars/',
        verbose_name='Фото профиля', help_text='Фото профиля.')
    role = models.CharField(
        max_length=MAX_TITLE,
        choices=ROLE_CHOICES_LIST,
        default=ROLE_CHOICES['user'],
        blank=True,
        verbose_name='роль')

    @property
    def is_admin(self):
        return self.role == ROLE_CHOICES['admin']

    @property
    def is_moderator(self):
        return self.role == ROLE_CHOICES['moderator']

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self) -> str:
        return self.username


class Project(models.Model):
    """
    Проект с датой начала, заверщения и файлом проекта.
    """
    title = models.CharField(
        max_length=MAX_TITLE,
        verbose_name='Проект', help_text='Название проекта')
    description = models.TextField(
        verbose_name='Описание', help_text='Описание проекта.')
    start_time = models.DateField(
        verbose_name='Начало проекта', help_text='Дата начала проекта.')
    end_time = models.DateField(
        verbose_name='Окончание проекта', help_text='Дата завершения проекта.')
    file = models.FileField(
        upload_to='files/',
        blank=True,
        verbose_name='Файл проекта', help_text='Файл проекта.')

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    """
    Задачи для проектов с датами, приоритетом и ответственным пользователем.
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=MAX_TITLE,
        verbose_name='Задача',
        help_text='Название задачи должно быть кратким и информативным.')
    description = models.TextField(
        verbose_name='Описание',
        help_text=(
            'Описание задачи должно содержать всю необходимую информацию.'))
    start_date = models.DateTimeField(
        verbose_name='Начало задачи', help_text='Дата начала задачи.')
    end_date = models.DateTimeField(
        verbose_name='Окончание задачи', help_text='Дата окончания задачи.')
    priority = models.IntegerField(
        verbose_name='Приоритет', help_text='Приоритет задачи от 1 до 5.')
    assignee = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Ответственный',
        help_text='Пользователь, ответственный за выполнение задачи.')

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    """
    Комментарии к задачам.
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'комментарии'
        verbose_name_plural = 'комментарий'

    def __str__(self) -> str:
        return self.text


class Attachment(models.Model):
    """
    Связаная модель зачади с файлом проекта.
    """
    file = models.FileField(upload_to='files/')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
