# Generated by Django 3.1 on 2020-08-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtegory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]