# Generated by Django 4.1.7 on 2023-03-04 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0007_remove_follow_following_user_remove_follow_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='surname',
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
