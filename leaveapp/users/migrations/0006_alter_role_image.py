# Generated by Django 4.0.6 on 2022-08-30 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_role_address_role_image_role_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
