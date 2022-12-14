# Generated by Django 4.1.3 on 2022-11-23 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0004_alter_esquadrao_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='esquadrao',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='esquadrao',
            name='logo',
            field=models.ImageField(blank=True, upload_to='foto/%d%m/%Y'),
        ),
    ]
