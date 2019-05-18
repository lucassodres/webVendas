from django.contrib.auth.models import User
from django.db import models

from cadastros.colaboradores.models import Colaboradores
from cadastros.empresas.models import Empresas


# ======================================================================================================================
#           CRIAR TABELA DE PERMISSOES DE CADA USUARIO PARA SUA EMPRESA E O CONSTRUTOR
# ======================================================================================================================


class Permissoes(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=40)

    administrador = models.IntegerField(default=0)
    administrador_super = models.IntegerField(default=0)

    cadastra_colaborador = models.IntegerField(default=0)
    edita_colaborador = models.IntegerField(default=0)
    acessa_cadastro_colaborador = models.IntegerField(default=0)
    muda_status_colaborador = models.IntegerField(default=0)

    cadastra_cliente = models.IntegerField(default=0)
    edita_cliente = models.IntegerField(default=0)
    acessa_cadastro_cliente = models.IntegerField(default=0)
    muda_status_cliente = models.IntegerField(default=0)

    cadastra_fornecedor = models.IntegerField(default=0)
    edita_fornecedor = models.IntegerField(default=0)
    acessa_cadastro_fornecedor = models.IntegerField(default=0)
    muda_status_fornecedor = models.IntegerField(default=0)

    cadastra_produto = models.IntegerField(default=0)
    edita_produto = models.IntegerField(default=0)
    acessa_cadastro_produto = models.IntegerField(default=0)
    muda_status_produto = models.IntegerField(default=0)
    altera_preco_produto = models.IntegerField(default=0)
    anuncia_produto = models.IntegerField(default=0)

    tabela_preco = models.IntegerField(default=0)
    edita_tabela_de_precos = models.IntegerField(default=0)
    acessa_tabela_de_precos = models.IntegerField(default=0)
    exclui_preco_tabelado = models.IntegerField(default=0)
    muda_status_preco_tabelado = models.IntegerField(default=0)

    registra_venda = models.IntegerField(default=0)
    edita_venda = models.IntegerField(default=0)
    fecha_venda = models.IntegerField(default=0)
    acessa_registro_venda = models.IntegerField(default=0)
    muda_status_venda = models.IntegerField(default=0)
    cancela_venda = models.IntegerField(default=0)
    imprime_cupom_de_venda = models.IntegerField(default=0)

    registra_compra = models.IntegerField(default=0)
    edita_compra = models.IntegerField(default=0)
    acessa_registro_compra = models.IntegerField(default=0)
    muda_status_compra = models.IntegerField(default=0)
    cancela_compra = models.IntegerField(default=0)
    finalizar_compra = models.IntegerField(default=0)

    registra_entrada_produto = models.IntegerField(default=0)
    edita_entrada_produto = models.IntegerField(default=0)
    acessa_entrada_produto = models.IntegerField(default=0)
    muda_status_entrada_produto = models.IntegerField(default=0)
    cancela_entrada_produto = models.IntegerField(default=0)

    registra_saida_produto = models.IntegerField(default=0)
    edita_saida_produto = models.IntegerField(default=0)
    acessa_saida_produto = models.IntegerField(default=0)
    muda_status_saida_produto = models.IntegerField(default=0)
    cancela_saida_produto = models.IntegerField(default=0)

    edita_contas_pagar = models.IntegerField(default=0)
    acessa_contas_pagar = models.IntegerField(default=0)
    exclui_contas_pagar = models.IntegerField(default=0)
    quita_contas_pagar = models.IntegerField(default=0)

    edita_contas_receber = models.IntegerField(default=0)
    acessa_contas_receber = models.IntegerField(default=0)
    exclui_contas_receber = models.IntegerField(default=0)
    quita_contas_receber = models.IntegerField(default=0)

    registra_pagamento = models.IntegerField(default=0)
    edita_pagamento = models.IntegerField(default=0)
    acessa_pagamento = models.IntegerField(default=0)
    muda_status_pagamento = models.IntegerField(default=0)
    exclui_pagamento = models.IntegerField(default=0)

    registra_recebimento = models.IntegerField(default=0)
    edita_recebimento = models.IntegerField(default=0)
    acessa_recebimento = models.IntegerField(default=0)
    muda_status_recebimento = models.IntegerField(default=0)
    exclui_recebimento = models.IntegerField(default=0)

    observacoes = models.TextField(max_length=200, blank=True)
    status = models.CharField(max_length=10, default='ATIVO')

    empresa = models.ForeignKey(Empresas, on_delete=models.DO_NOTHING, default=0)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+', '+str(self.descricao)+', '+self.empresa.razao_social


    class Meta:
        db_table = 'permissao'
        ordering = ('descricao',)

# ======================================================================================================================
#    CRIAR TABELA DE USUARIOS, CONSTRUTOR DA CLASSE E METODO PRA SALVAR USUARIOS CORRELATAMENTE AO MODEL USERS DO DJANGO
# ======================================================================================================================


class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, blank=True, null=True, on_delete=models.DO_NOTHING,)
    colaborador = models.ForeignKey(Colaboradores, blank=True, null=True, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=30, blank=True, null=True)
    sobre_nome = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=False, unique=True)
    status = models.CharField('Status', max_length=10, default='ATIVO', blank=False, null=False, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO'),
    ))
    observacoes = models.TextField(max_length=200, blank=True, null=True)
    empresa = models.ForeignKey(Empresas, on_delete=models.DO_NOTHING)
    permissoes = models.ForeignKey(Permissoes, on_delete=models.DO_NOTHING)
    model_template = models.CharField(max_length=100, blank=True, null=True)
    data_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True, null=True)


    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'usuarios'
        ordering = ('nome',)


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        senha = self.email.replace('.', '').replace('@', '')
        if not self.pk:
            user = User.objects.filter(username=self.email)
            if not user.count():
                user = User.objects.create_user(self.email, self.email, senha)
                user.save()
            self.usuario = user
        else:
            if not self.usuario:
                user = User.objects.filter(username=self.email)
                if not user.count:
                    user = User.objects.create_user(self.email, self.email, senha)
                    user.save()
                self.usuario = user
            else:
                self.usuario.username = self.email
                self.usuario.email = self.email
        super(Usuarios, self).save()
