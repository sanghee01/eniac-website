# Generated by Django 3.2.7 on 2022-01-13 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='tag',
            field=models.ManyToManyField(to='tags.Tag', verbose_name='태그'),
        ),
    ]