# Generated by Django 4.0.6 on 2022-07-12 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_alter_contract_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthstatus',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='work.contract', verbose_name='Договор'),
        ),
    ]
