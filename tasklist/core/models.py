from django.db import models

STATUS = (
    ('Backlog', 'Backlog'),
    ('A fazer', 'A fazer'),
    ('Fazendo', 'Fazendo'),
    ('Feito', 'Feito')
)


class TaskList(models.Model):
    title = models.CharField('Titulo', max_length=120)
    desc = models.CharField('Descrição', max_length=1000, blank=False)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(blank=True)
    status = models.CharField('Status', choices=STATUS, default='1', max_length=30)
