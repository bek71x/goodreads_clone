# Generated by Django 5.1.6 on 2025-03-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='profile_pictures/default.png', upload_to='profile_pictures'),
        ),
    ]
