# Generated by Django 4.2.1 on 2023-06-25 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_contact_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male'), ('others', 'others')], max_length=10, null=True),
        ),
    ]
