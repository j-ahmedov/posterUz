# Generated by Django 4.1.7 on 2023-02-21 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0004_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
