# Generated by Django 3.2.7 on 2022-01-03 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_content', models.CharField(max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='notice',
            name='tagging',
            field=models.ManyToManyField(null=True, related_name='tagged', to='notices.Tag'),
        ),
    ]