# Generated by Django 5.1.3 on 2024-11-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.ImageField(default='profile/default.webp', upload_to='profile'),
        ),
    ]