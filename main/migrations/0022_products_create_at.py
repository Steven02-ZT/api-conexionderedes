# Generated by Django 4.2.1 on 2023-05-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_rename_high_products_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='create_at',
            field=models.DateField(auto_now_add=True),
            preserve_default=False,
        ),
    ]