# Generated by Django 4.2.7 on 2023-12-03 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='created')),
                ('status', models.CharField(choices=[('BG', 'Bug'), ('WK', 'Work'), ('DN', 'Done')], default='DN', max_length=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_issues', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
                'indexes': [models.Index(fields=['created'], name='board_issue_created_c96a18_idx')],
            },
        ),
    ]