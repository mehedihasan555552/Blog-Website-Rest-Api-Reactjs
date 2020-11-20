# Generated by Django 3.0.6 on 2020-11-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201119_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomments',
            name='author',
        ),
        migrations.AddField(
            model_name='blogcomments',
            name='ip',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogcomments',
            name='name',
            field=models.CharField(default='Annoymous', max_length=255),
        ),
    ]