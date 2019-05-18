# Generated by Django 2.2.1 on 2019-05-16 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
        ('contas_pagar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pagamento', models.DateField(blank=True, null=True)),
                ('data_vencimento', models.DateField(blank=True, null=True)),
                ('valor_pagamento', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status_pagamento', models.CharField(choices=[('PENDENTE', 'PENDENTE'), ('PAGO', 'PAGO'), ('PARCIALMENTE PAGO', 'PARCIALMENTE PAGO'), ('CANCELADO', 'CANCELADO')], max_length=20)),
                ('meio_pagamento', models.CharField(choices=[('DINHEIRO', 'DINHEIRO'), ('CARTAO DEBITO', 'CARTAO DEBITO'), ('CARTAO CREDITO', 'CARTAO CREDITO'), ('CHEQUE', 'CHEQUE'), ('OUTROS', 'OUTROS')], max_length=15)),
                ('observacoes_pagamento', models.CharField(blank=True, max_length=200)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas_pagar.ContasPagar')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresas.Empresas')),
            ],
            options={
                'db_table': 'pagamentos',
                'ordering': ('data_vencimento', 'valor_pagamento'),
            },
        ),
    ]