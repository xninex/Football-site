# Generated by Django 4.1.3 on 2022-11-28 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='latestnewsmodel',
            options={'verbose_name': 'Последняя новость', 'verbose_name_plural': 'Последние новости'},
        ),
        migrations.AlterField(
            model_name='latestnewsmodel',
            name='content',
            field=models.TextField(verbose_name='Текст новости'),
        ),
        migrations.AlterField(
            model_name='latestnewsmodel',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='latestnewsmodel',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя комментатора')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.latestnewsmodel')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
