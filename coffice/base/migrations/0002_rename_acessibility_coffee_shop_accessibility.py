# Generated by Django 5.0.4 on 2024-04-22 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffee_shop',
            old_name='acessibility',
            new_name='accessibility',
        ),
    ]