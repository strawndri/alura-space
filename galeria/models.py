from django.db import models

class Fotografia(models.Model):

    OPCOES_DE_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')
    ]

    # colunas da tabela Fotografia
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_DE_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    # boa prática
    def __str__(self):
        return f'Fotografia [nome={self.nome}]'