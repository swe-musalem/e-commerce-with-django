# Generated by Django 4.0 on 2022-09-20 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='id',
            new_name='proudctId',
        ),
    ]
