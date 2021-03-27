from django.db import models

# Create your models here.
class Turma(models.Model):
    def __str__(self):
        return self.nome

    TURNOS_OPTIONS = [
        ('matutino','Matutino'),
        ('vespertino','Vespertino'),
        ('noturno','Noturno'),
    ]
    nome = models.CharField(max_length=30)
    turno = models.CharField(max_length=30, choices=TURNOS_OPTIONS)
    ordem = models.PositiveSmallIntegerField()

class Horario(models.Model):
    class Meta:
        ordering=['dia_semana', 'inicio']
    def __str__(self):
        return '{} : {}-{}'.format(self.get_dia_semana_display(), self.inicio, self.termino)

    DAYS_OF_WEEK = (
    (1, 'SEG'),
    (2, 'TER'),
    (3, 'QUA'),
    (4, 'QUI'),
    (5, 'SEX'),
    (6, 'SAB'),
    (7, 'DOM'),
    )
    turma = models.ForeignKey(Turma, related_name='horarios', on_delete=models.CASCADE)
    dia_semana = models.IntegerField(choices=DAYS_OF_WEEK)
    inicio = models.TimeField()
    termino = models.TimeField()
    disciplina = models.CharField(max_length=50)
    professor = models.CharField(max_length=60)
    link = models.CharField(max_length=100, null=True, blank=True)