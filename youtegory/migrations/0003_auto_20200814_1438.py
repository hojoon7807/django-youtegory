# Generated by Django 3.1 on 2020-08-14 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtegory', '0002_category_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='youtegory.category'),
        ),
    ]