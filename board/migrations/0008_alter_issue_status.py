# Generated by Django 4.2.7 on 2023-12-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_issue_type_alter_issue_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('In Progress', 'In Progress'), ('Complete', 'Complete')], default='Complete', max_length=20),
        ),
    ]
