# Generated by Django 3.0.9 on 2020-08-04 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtegory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
