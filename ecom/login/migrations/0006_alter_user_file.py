# Generated by Django 5.0.6 on 2024-07-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_alter_user_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='file',
            field=models.FileField(max_length=230, upload_to='uploads/'),
        ),
    ]
