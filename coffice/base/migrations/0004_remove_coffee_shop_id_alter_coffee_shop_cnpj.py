# Generated by Django 5.0.3 on 2024-04-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_coffee_shop_rating_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee_shop',
            name='id',
        ),
        migrations.AlterField(
            model_name='coffee_shop',
            name='cnpj',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
