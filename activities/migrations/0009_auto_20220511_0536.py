# Generated by Django 3.2.7 on 2022-05-11 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0008_rename_activities_act_comment_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act_comment',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comm', to='activities.activity'),
        ),
        migrations.AlterField(
            model_name='act_comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_users', to=settings.AUTH_USER_MODEL),
        ),
    ]