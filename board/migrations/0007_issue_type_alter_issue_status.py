# Generated by Django 4.2.7 on 2023-12-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_alter_issue_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='type',
            field=models.CharField(choices=[('Task', 'Task'), ('Critical', 'Critical'), ('New Feature', 'Feature')], default='Task', max_length=20),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('In Progress', 'Work'), ('Complete', 'Done')], default='In Progress', max_length=20),
        ),
    ]
