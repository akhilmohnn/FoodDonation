# Generated by Django 5.0 on 2024-01-26 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_tbl_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_organization',
            name='status',
            field=models.CharField(default=0, max_length=50, null=True),
        ),
    ]
