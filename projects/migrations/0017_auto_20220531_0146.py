# Generated by Django 3.2.7 on 2022-05-31 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_project_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='img_a',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지1'),
        ),
        migrations.AddField(
            model_name='project',
            name='img_b',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지2'),
        ),
        migrations.AddField(
            model_name='project',
            name='img_c',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지3'),
        ),
    ]
