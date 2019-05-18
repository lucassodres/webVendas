# Generated by Django 2.2.1 on 2019-05-16 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('produtos', '0001_initial'),
        ('empresas', '0001_initial'),
        ('contas_receber', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('solicitante', models.CharField(max_length=50, verbose_name='Solicitante')),
                ('data_venda', models.DateField(auto_now_add=True)),
                ('data_entrega', models.DateField()),
                ('vencimento', models.DateField(auto_now_add=True)),
                ('status_pedido', models.CharField(default='EM ANDAMENTO', max_length=30, verbose_name='Státus do Pedido')),
                ('valor_total', models.DecimalField(decimal_places=2, default='0', max_digits=15, verbose_name='Valor total')),
                ('desconto', models.DecimalField(decimal_places=2, default='0', max_digits=15, verbose_name='Desconto')),
                ('saldo_final', models.DecimalField(decimal_places=2, default='0', max_digits=15, verbose_name='Saldo final')),
                ('observacoes', models.TextField(blank=True, max_length=200, verbose_name='Observações')),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('cep', models.CharField(blank=True, max_length=10, verbose_name='CEP')),
                ('endereco', models.CharField(blank=True, max_length=50, verbose_name='Endereço')),
                ('numero', models.CharField(blank=True, max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=30)),
                ('bairro', models.CharField(blank=True, max_length=50, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, max_length=2, verbose_name='Estado')),
                ('observacoes_entrega', models.TextField(blank=True, max_length=200, verbose_name='Observações')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Clientes')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresas.Empresas')),
                ('pagamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contas_receber.ContasReceber')),
            ],
            options={
                'db_table': 'vendas',
                'ordering': ('-data_venda',),
            },
        ),
        migrations.CreateModel(
            name='SaidaProdutos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=3, max_digits=15, verbose_name='Quantidade')),
                ('data_saida', models.DateField(auto_now_add=True)),
                ('valor_unitario', models.DecimalField(decimal_places=3, default='0', max_digits=15, verbose_name='Valor unitário')),
                ('percentual_desconto', models.DecimalField(decimal_places=3, default='0', max_digits=15, verbose_name='Desconto %')),
                ('total_desconto', models.DecimalField(decimal_places=2, default='0', max_digits=15, verbose_name='Desconto total')),
                ('valor_total', models.DecimalField(decimal_places=2, default='0', max_digits=15, verbose_name='Valor total')),
                ('status', models.CharField(choices=[('EM SEPARACAO', 'EM SEPARACAO'), ('SEPARADO', 'SEPARADO'), ('ENTREGUE', 'ENTREGUE'), ('CANCELADO', 'CANCELADO')], default='AGUARDANDO', max_length=20, verbose_name='Státus')),
                ('balanco', models.CharField(choices=[('ABERTO', 'ABERTO'), ('FECHADO', 'FECHADO')], default='ABERTO', max_length=20, verbose_name='Balanço')),
                ('observacoes_saida', models.TextField(blank=True, max_length=200, verbose_name='Observações')),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('saldo_final', models.DecimalField(decimal_places=2, default='0', max_digits=15)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresas.Empresas')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Produtos')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.Vendas', verbose_name='Nome/Razão social:')),
            ],
            options={
                'db_table': 'saida_produtos',
                'ordering': ('-data_saida',),
            },
        ),
    ]
