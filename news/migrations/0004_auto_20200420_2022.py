# Generated by Django 3.0.5 on 2020-04-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200420_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(max_length=250),
        ),
    ]
