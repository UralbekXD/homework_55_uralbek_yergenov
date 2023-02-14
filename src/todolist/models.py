from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=4096, null=False, blank=False, verbose_name='Описание')

    NEW = 'new'
    IN_PROGRESS = 'in progress'
    DONE = 'done'
    STATUS_CHOICES = [
        (NEW, 'Новый'),
        (IN_PROGRESS, 'В процессе'),
        (DONE, 'Сделано'),
    ]
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
