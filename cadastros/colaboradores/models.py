from django.contrib.auth.models import User
from django.db import models
from cadastros.empresas.models import Empresas

# ======================================================================================================================
#           CRIAR TABELA DE COLABORADORES E O CONSTRUTOR
# ======================================================================================================================


class Colaboradores(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=False)
    sobre_nome = models.CharField(max_length=30, blank=False)
    rg = models.CharField(max_length=15, blank=True)
    cpf = models.CharField(max_length=15, blank=True)
    telefone = models.CharField(max_length=30, blank=True)
    celular = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    estado_civil = models.CharField(max_length=15, blank=False, null=False, choices=(
        ('SOLTEIRO', 'SOLTEIRO'),
        ('CASADO', 'CASADO'),
        ('VIUVO', 'VIUVO'),
        ('DIVORCIADO', 'DIVORCIADO'),
        ('SEPARADO', 'SEPARADO'),
        ('UNIAO ESTAVEL', 'UNIAO ESTAVEL'),

    ))
    sexo = models.CharField('Sexo', max_length=15, blank=False, null=False, choices=(
        ('MASCULINO', 'MASCULINO'),
        ('FEMININO', 'FEMININO'),
    ))
    cep = models.CharField('cep', max_length=10, blank=True)
    endereco = models.CharField('endereco', max_length=50, blank=True)
    numero = models.CharField('numero', max_length=10, blank=True)
    complemento = models.CharField('complemento', max_length=50, blank=True)
    bairro = models.CharField('bairro', max_length=50, blank=True)
    cidade = models.CharField('cidade', max_length=50, blank=True)
    estado = models.CharField('estado', max_length=50, blank=True)
    status = models.CharField('status', max_length=15, blank=False, null=False, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO'),
        ('AFASTADO', 'AFASTADO'),
        ('APOSENTADO', 'APOSENTADO'),
        ('DESLIGADO', 'DESLIGADO'),
    ))
    observacoes = models.TextField(max_length=200, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    empresa = models.ForeignKey(Empresas, on_delete=models.DO_NOTHING)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'colaboradores'
        ordering = ('nome',)