# Generated by Django 3.2.7 on 2022-03-11 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_merge_20220301_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
