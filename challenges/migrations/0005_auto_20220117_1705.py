# Generated by Django 2.2.5 on 2022-01-17 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0004_auto_20211231_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='challenge_comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
