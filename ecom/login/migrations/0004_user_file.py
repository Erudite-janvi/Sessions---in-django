# Generated by Django 5.0.6 on 2024-07-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_user_email_alter_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='file',
            field=models.FileField(default='default_file_path', max_length=23, upload_to=''),
        ),
    ]
