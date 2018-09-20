# Generated by Django 2.0.2 on 2018-09-15 18:29

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url_title', models.CharField(default='', editable=False, max_length=255)),
                ('summary', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', markdownx.models.MarkdownxField()),
                ('published', models.BooleanField(default=False)),
                ('published_at', models.DateTimeField(blank=True)),
                ('tags', models.ManyToManyField(blank=True, to='tags.Tag')),
            ],
            options={
                'ordering': ['-published_at', '-created_at'],
            },
        ),
    ]
