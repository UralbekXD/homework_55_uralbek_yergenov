from django.db import models


NEW = 'new'
IN_PROGRESS = 'in progress'
DONE = 'done'
STATUS_CHOICES = [
    (NEW, 'Новый'),
    (IN_PROGRESS, 'В процессе'),
    (DONE, 'Сделано'),
]


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False, verbose_name='Заголовок')
    description = models.CharField(max_length=128, null=False, blank=False, verbose_name='Описание')
    full_description = models.TextField(max_length=4096, null=True, blank=True, verbose_name='Полное описание')

    status = models.CharField(
        max_length=16,
        null=False,
        blank=False,
        verbose_name='Статус',
        choices=STATUS_CHOICES,
        default=NEW,
    )

    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.pk} {self.title} {self.status} {self.deadline}'
