from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ClosedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


# Create your models here.
class Issue(models.Model):
    class Type(models.TextChoices):
        TASK = 'Task'
        CRITICAL = 'Critical'
        FEATURE = 'New Feature'

    class Status(models.TextChoices):
        IN_PROGRESS = 'In Progress'
        COMPLETE = 'Complete'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='created')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_issues')
    type = models.CharField(max_length=20, choices=Type.choices, default=Type.TASK)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.COMPLETE)
    objects = models.Manager()
    closed = ClosedManager()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    # tags = TaggableManager()

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title.lower().replace(' ', '-')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('board:issue_detail',
                       args=[self.created.year, self.created.month, self.created.day, self.slug])
