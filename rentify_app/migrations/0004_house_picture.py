# Generated by Django 4.2.13 on 2024-05-19 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentify_app', '0003_alter_house_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='house_pics'),
        ),
    ]
