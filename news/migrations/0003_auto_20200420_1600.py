# Generated by Django 3.0.5 on 2020-04-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_autor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['name', 'email']},
        ),
        migrations.AddField(
            model_name='autor',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]