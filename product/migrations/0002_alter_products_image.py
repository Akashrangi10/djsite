# Generated by Django 3.2.23 on 2024-01-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]