# Generated by Django 5.0 on 2024-01-05 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_tbl_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_name', models.CharField(max_length=50)),
            ],
        ),
    ]
