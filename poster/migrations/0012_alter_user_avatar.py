# Generated by Django 4.1.7 on 2023-08-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0011_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/%Y/%m/%d/'),
        ),
    ]
