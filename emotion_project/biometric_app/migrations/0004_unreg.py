# Generated by Django 4.0.3 on 2022-05-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biometric_app', '0003_delete_unreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='unreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=None)),
            ],
        ),
    ]
