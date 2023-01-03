# Generated by Django 4.1.4 on 2023-01-02 11:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('author', models.CharField(max_length=50)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('author', models.CharField(max_length=50)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(db_column='article', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='api.article')),
                ('root_comment', models.ForeignKey(db_column='root_comment', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='api.comment')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['id'], name='article_id_3f42b6_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['id', 'article'], name='comment_id_c9ab80_idx'),
        ),
    ]
