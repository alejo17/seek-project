from django.db import models


class Task(models.Model):
    TO_DO = 'TD'
    IN_PROGRESS = 'IP'
    COMPLETED = 'C'
    STATES = [
        (TO_DO, 'Por hacer'),
        (IN_PROGRESS, 'En progreso'),
        (COMPLETED, 'Completada'),
    ]

    title = models.CharField(
        'title', max_length=150, blank=True)
    description = models.CharField(
        'description', max_length=250, blank=True)
    state = models.CharField(
        'estado', choices=STATES, max_length=2, default=TO_DO)
    

    def __str__(self):
        return self.title