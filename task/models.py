from django.db import models
from model_utils import Choices
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    STATUSES = Choices(
        (0,  _('pending')),
        (1,  _('completed'))
    )
    status = models.IntegerField(choices=STATUSES, default=0)
    def __str__(self):
        return self.title