# Generated by Django 4.1.3 on 2022-11-23 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0005_esquadrao_link_esquadrao_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='esquadrao',
            name='link',
        ),
        migrations.AlterField(
            model_name='esquadrao',
            name='logo',
            field=models.ImageField(blank=True, upload_to='foto/%d/%m/%Y'),
        ),
    ]