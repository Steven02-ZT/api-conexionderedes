# Generated by Django 4.2.1 on 2023-05-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_category_object_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='brand',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
