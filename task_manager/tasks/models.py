from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.


class Task(models.Model):
    name = models.CharField(_('name'), max_length=30)
    description = models.TextField(_('description'), blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name=_('status'))
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
        blank=True,
        verbose_name=_('author')
    )
    executor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='executor',
        blank=True,
        null=True,
        verbose_name=_('executor')
    )
    created_at = models.DateTimeField(_("created_at"), default=timezone.now)
    labels = models.ManyToManyField(
        Label,
        through='TaskLabel',
        related_name='labels',
        verbose_name=_('labels'),
        blank=True,
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
