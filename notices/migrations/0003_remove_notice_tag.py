# Generated by Django 3.2.7 on 2022-01-14 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_notice_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='tag',
        ),
    ]