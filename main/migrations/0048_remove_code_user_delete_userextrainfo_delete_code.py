# Generated by Django 4.2.1 on 2023-09-04 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_product_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserExtraInfo',
        ),
        migrations.DeleteModel(
            name='Code',
        ),
    ]
