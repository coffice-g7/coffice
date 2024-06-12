# Generated by Django 5.0.6 on 2024-05-25 04:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_coffee_shop_id_alter_coffee_shop_cnpj'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('like', 'Like'), ('unlike', 'Unlike')], max_length=10)),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.coffee_shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('coffee', 'user')},
            },
        ),
    ]
