# Generated by Django 3.2.4 on 2021-06-18 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_alter_market_redirect_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='redirect_permanently',
            field=models.BooleanField(null=True, verbose_name='انتقال دائم'),
        ),
    ]
