# Generated by Django 3.2.7 on 2023-05-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city360', '0002_auto_20230418_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='wrkregg',
            name='file',
            field=models.FileField(default=0, max_length=150, upload_to=''),
            preserve_default=False,
        ),
    ]
