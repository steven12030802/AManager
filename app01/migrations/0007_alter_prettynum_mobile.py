# Generated by Django 4.0.4 on 2022-04-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prettynum',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='资产名称'),
        ),
    ]
