# Generated by Django 4.2.14 on 2024-07-25 06:45

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(help_text='Имя пользователя.', max_length=100, unique=True, verbose_name='Заголовок')),
                ('email', models.EmailField(help_text='Электронная почта.', max_length=254, verbose_name='Электронная почта')),
                ('password', models.CharField(help_text='Пароль.', max_length=100, verbose_name='Пароль')),
                ('avatar', models.ImageField(help_text='Фото профиля.', upload_to='avatars/', verbose_name='Фото профиля')),
                ('role', models.CharField(blank=True, choices=[('user', 'user'), ('admin', 'admin'), ('moderator', 'moderator')], default='user', max_length=100, verbose_name='роль')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название проекта', max_length=100, verbose_name='Проект')),
                ('description', models.TextField(help_text='Описание проекта.', verbose_name='Описание')),
                ('start_time', models.DateField(help_text='Дата начала проекта.', verbose_name='Начало проекта')),
                ('end_time', models.DateField(help_text='Дата завершения проекта.', verbose_name='Окончание проекта')),
                ('file', models.FileField(help_text='Файл проекта.', upload_to='files/', verbose_name='Файл проекта')),
            ],
            options={
                'verbose_name': 'проект',
                'verbose_name_plural': 'проекты',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название задачи должно быть кратким и информативным.', max_length=100, verbose_name='Задача')),
                ('description', models.TextField(help_text='Описание задачи должно содержать всю необходимую информацию.', verbose_name='Описание')),
                ('start_date', models.DateTimeField(help_text='Дата начала задачи.', verbose_name='Начало задачи')),
                ('end_date', models.DateTimeField(help_text='Дата окончания задачи.', verbose_name='Окончание задачи')),
                ('priority', models.IntegerField(help_text='Приоритет задачи от 1 до 5.', verbose_name='Приоритет')),
                ('assignee', models.ForeignKey(help_text='Пользователь, ответственный за выполнение задачи.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ответственный')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project')),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'задачи',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.task')),
            ],
            options={
                'verbose_name': 'комментарии',
                'verbose_name_plural': 'комментарий',
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.task')),
            ],
        ),
    ]
