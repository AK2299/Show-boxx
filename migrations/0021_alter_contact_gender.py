# Generated by Django 4.2.1 on 2023-10-24 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_alter_contact_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('others', 'others'), ('female', 'female')], max_length=10, null=True),
        ),
    ]
