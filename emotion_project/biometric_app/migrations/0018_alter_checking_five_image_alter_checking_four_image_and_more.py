# Generated by Django 4.0.3 on 2022-05-28 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biometric_app', '0017_checking_five_checking_four_checking_one_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checking_five',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='biometric_app/five'),
        ),
        migrations.AlterField(
            model_name='checking_four',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='biometric_app/four'),
        ),
        migrations.AlterField(
            model_name='checking_one',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='biometric_app/one'),
        ),
        migrations.AlterField(
            model_name='checking_three',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='biometric_app/three'),
        ),
        migrations.AlterField(
            model_name='checking_two',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='biometric_app/two'),
        ),
    ]
