# Generated by Django 4.2.1 on 2023-05-25 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_products_category_products_categorys'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='categorys',
        ),
    ]