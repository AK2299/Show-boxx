# Generated by Django 4.2.1 on 2023-06-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.CharField(choices=[('female', 'female'), ('others', 'others'), ('male', 'male')], max_length=10, null=True),
        ),
    ]
