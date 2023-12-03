from django.db import models
from django.contrib.auth.models import User


class ClosedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


# Create your models here.
class Issue(models.Model):
    class Status(models.TextChoices):
        BUG = 'BUG', 'Bug'
        WORK = 'WORK', 'Work'
        DONE = 'DONE', 'Done'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='created')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_issues')
    status = models.CharField(max_length=5, choices=Status.choices, default=Status.BUG)
    objects = models.Manager()
    closed = ClosedManager()
    created = models.DateTimeField(auto_now_add=True)
    #tags = TaggableManager()

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return self.title
