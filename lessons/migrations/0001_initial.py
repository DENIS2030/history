# Generated by Django 3.2.3 on 2021-06-02 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Класс')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название Учебника')),
                ('image', models.ImageField(upload_to='books/', verbose_name='Изображение для категории')),
                ('bookurl', models.TextField(blank=True, null=True, verbose_name='Ссылка на учебник')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название категории')),
                ('description', models.TextField(verbose_name='Описание категории')),
                ('image', models.ImageField(upload_to='lessons/', verbose_name='Изображение для категории')),
            ],
        ),
        migrations.CreateModel(
            name='Elective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('url', models.SlugField(max_length=130, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ElectiveCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название категории')),
                ('description', models.TextField(verbose_name='Описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название урока')),
                ('presentation', models.TextField(blank=True, null=True, verbose_name='Ссылка на презентацию')),
                ('image', models.ImageField(upload_to='lessons/', verbose_name='Изображение для категории')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.age', verbose_name='Класс')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.books', verbose_name='Книга')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Pharagraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст урока')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='Урок')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='фильм')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lessons.reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарий',
            },
        ),
        migrations.CreateModel(
            name='PharagraphImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='lessons/', verbose_name='Изображение для категории')),
                ('pharagraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.pharagraph', verbose_name='Урок')),
            ],
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('multimedia', models.TextField(blank=True, null=True, verbose_name='Ссылка на видео')),
                ('elective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.elective', verbose_name='Факультатив')),
            ],
        ),
        migrations.CreateModel(
            name='LearnApps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.TextField(verbose_name='Ссылка на задание')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='Урок')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='Изображение для категории')),
                ('check', models.BooleanField(default=False)),
                ('elective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.elective', verbose_name='Категория')),
            ],
        ),
        migrations.AddField(
            model_name='elective',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.electivecategory', verbose_name='Категория'),
        ),
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст урока')),
                ('video', models.TextField(blank=True, null=True, verbose_name='Ссылка на видео')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='Урок')),
            ],
        ),
    ]
