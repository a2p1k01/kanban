# Generated by Django 4.2.7 on 2023-12-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_issue_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['created']},
        ),
        migrations.RemoveIndex(
            model_name='issue',
            name='board_issue_created_622907_idx',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='created_at',
            new_name='created',
        ),
        migrations.AddIndex(
            model_name='issue',
            index=models.Index(fields=['created'], name='board_issue_created_c96a18_idx'),
        ),
    ]
