# Generated by Django 4.0.6 on 2022-07-31 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(),
        ),
    ]
