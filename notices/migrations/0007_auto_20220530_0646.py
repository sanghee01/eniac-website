# Generated by Django 3.2.7 on 2022-05-30 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0006_auto_20220530_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='img_a',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지1'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='img_b',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지2'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='img_c',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지3'),
        ),
    ]
