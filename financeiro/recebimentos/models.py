from django.db import models
from cadastros.empresas.models import Empresas
from financeiro.contas_receber.models import ContasReceber
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible  # esta linha somente e necessario quando usado python2.x
class Recebimentos(models.Model):
    data_recebimento = models.DateField(blank=True, null=True)
    data_vencimento = models.DateField(blank=True, null=True)
    valor_recebimento = models.DecimalField(max_digits=15, decimal_places=2)
    status_recebimento = models.CharField(max_length=20, blank=False,
                                        choices=(('PENDENTE', 'PENDENTE'),
                                                 ('PAGO', 'PAGO'),
                                                 ('PARCIALMENTE PAGO', 'PARCIALMENTE PAGO'),
                                                 ('CANCELADO', 'CANCELADO')
                                                 ))
    meio_recebimento = models.CharField(max_length=15, blank=False,
                                      choices=(('DINHEIRO', 'DINHEIRO'),
                                               ('CARTAO DEBITO', 'CARTAO DEBITO'),
                                               ('CARTAO CREDITO', 'CARTAO CREDITO'),
                                               ('CHEQUE', 'CHEQUE'),
                                               ('OUTROS', 'OUTROS')
                                               ))
    observacoes_recebimento = models.CharField(max_length=200, blank=True)
    conta = models.ForeignKey(ContasReceber, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresas, blank=True, null=True, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('data_vencimento', 'valor_recebimento')
        db_table = 'recebimentos'

    def __str__(self):
        data_vencimento = self.data_vencimento.strftime('%d/%m/%Y')
        valor_recebimento = '%0.02f' % self.valor_recebimento
        return '%s - %s (%s)' % (valor_recebimento, self.status_recebimento, data_vencimento)