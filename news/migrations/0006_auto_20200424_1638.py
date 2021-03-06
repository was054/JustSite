# Generated by Django 3.0.5 on 2020-04-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_autor_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['-data']},
        ),
        migrations.AddField(
            model_name='autor',
            name='data',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='autor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
