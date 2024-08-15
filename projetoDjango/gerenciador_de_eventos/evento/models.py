from django.db import models

# Create your models here.

class Evento(models.Model):
    TIPOS_EVENTO = [
        ('show', 'Shows'),
        ('stand_up', 'Stand Up'),
        ('teatro', 'Apresentações Teatrais'),
        ('aniversario', 'Aniversário de Itapajé'),
        # Adicione outros tipos conforme necessário
    ]

    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPOS_EVENTO)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gratuito = models.BooleanField(default=False)
    local = models.CharField(max_length=200)
    horario = models.TimeField()
    cidade = models.CharField(max_length=100)
    vagas = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    