from django.contrib.auth.models import User
from django.db import models

# ======================================================================================================================
#           CRIAR TABELA DE PLANOS E O CONSTRUTOR
# ======================================================================================================================


class Planos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('nome do plano', max_length=50, blank=False, unique=True)
    descricao = models.TextField('descricao do plano', max_length=100, blank=True)
    valor = models.DecimalField('valor', max_digits=15, blank=False, decimal_places=2, default=0)
    desconto_maximo = models.DecimalField('desconto maximo %', max_digits=15, blank=False, decimal_places=2, default=0)
    observacoes = models.TextField('observacoes', max_length=250, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.nome

    class Meta:
        db_table = 'planos'
        ordering = ('nome',)


# ======================================================================================================================
#           CRIAR TABELA DE EMPRESAS E O CONSTRUTOR
# ======================================================================================================================

class Empresas(models.Model):
    id = models.AutoField(primary_key=True)
    razao_social = models.CharField('razao social', max_length=50, blank=True, unique=True)
    nome_fantasia = models.CharField('nome fantasia', max_length=50, blank=False, unique=True)
    cnpj = models.CharField('cnpj', max_length=20, blank=True, unique=True)
    inscricao_estadual = models.CharField('inscricao estadual', max_length=20, blank=True, unique=True)
    inscricao_municipal = models.CharField('inscricao municipal', max_length=20, blank=True, unique=True)
    contato = models.CharField(max_length=30, blank=False)
    telefone = models.CharField(max_length=30, blank=True)
    celular = models.CharField(max_length=30, blank=True)
    email = models.EmailField('email', blank=True)
    site = models.CharField(max_length=50, blank=True)
    cep = models.CharField(max_length=9, blank=True)
    endereco = models.CharField(max_length=40, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=40, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    uf = models.CharField(max_length=2, blank=True)
    contato_cobranca = models.CharField(max_length=50, blank=True)
    telefone_cobranca = models.CharField(max_length=30, blank=True)
    celular_cobranca = models.CharField(max_length=30, blank=True)
    email_cobranca = models.EmailField('email', blank=True)
    cep_cobranca = models.CharField(max_length=9, blank=True)
    endereco_cobranca = models.CharField(max_length=40, blank=True)
    numero_cobranca = models.CharField(max_length=10, blank=True)
    complemento_cobranca = models.CharField(max_length=40, blank=True)
    bairro_cobranca = models.CharField(max_length=50, blank=True)
    cidade_cobranca = models.CharField(max_length=50, blank=True)
    uf_cobranca = models.CharField(max_length=2, blank=True)
    dia_pagamento = models.IntegerField(blank=True, null=True)
    plano = models.ForeignKey(Planos, on_delete=models.DO_NOTHING)
    forma_pagamento = models.CharField('forma pagamento', max_length=20, blank=False, choices=(
        ('A VISTA', 'A VISTA'),
        ('PARCELADO', 'PARCELADO'),
        ('FREE', 'FREE'),
    ))
    meio_pagamento = models.CharField('meio de pagamento', max_length=20, blank=False, choices=(
        ('BOLETO BANCARIO', 'BOLETO BANCARIO'),
        ('DEPOSITO EM CONTA', 'DEPOSITO EM CONTA'),
        ('CARTAO DE CREDITO', 'CARTAO DE CREDITO'),
        ('CARTAO DE DEBITO', 'CARTAO DE DEBITO'),
        ('GRATUIDADE', 'GRATUIDADE'),
        ('OUTROS', 'OUTROS'),
    ))
    status = models.CharField('status', max_length=20, blank=False, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('SUSPENSO', 'SUSPENSO'),
        ('EXCLUIDO', 'EXCLUIDO'),
        ('NEGATIVADO', 'NEGATIVADO'),

    ))
    data_inicio = models.DateField(blank=True, null=True)
    contrato = models.CharField('contrato', max_length=30, blank=True)
    observacoes = models.TextField(max_length=250, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nome_fantasia


    class Meta:
        db_table = 'empresas'
        ordering = ('nome_fantasia',)


class EmpresaResponsaveis(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.ForeignKey(Empresas, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    observacoes = models.TextField(max_length=250, blank=True)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.empresa

    class Meta:
        db_table = 'empresas_responsaveis'
        ordering = ('empresa',)

