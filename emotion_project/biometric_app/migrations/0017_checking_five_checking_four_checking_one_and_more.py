# Generated by Django 4.0.3 on 2022-05-28 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biometric_app', '0016_checking_alter_unreg_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checking_Five',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='biometric_app/check')),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Checking_Four',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='biometric_app/check')),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Checking_One',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='biometric_app/check')),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Checking_Three',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='biometric_app/check')),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Checking_Two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='biometric_app/check')),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
