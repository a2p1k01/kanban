# Generated by Django 4.2.7 on 2023-12-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_issue_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('Critical', 'Bug'), ('Feature', 'Feature'), ('In Progress', 'Work'), ('Complete', 'Done')], default='Critical', max_length=20),
        ),
    ]
