# Generated by Django 4.2.7 on 2023-12-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_issue_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['created_at']},
        ),
        migrations.RemoveIndex(
            model_name='issue',
            name='board_issue_created_c96a18_idx',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='closed',
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('BUG', 'Bug'), ('WORK', 'Work'), ('DONE', 'Done')], default='BUG', max_length=5),
        ),
        migrations.AddIndex(
            model_name='issue',
            index=models.Index(fields=['created_at'], name='board_issue_created_622907_idx'),
        ),
    ]