# Generated by Django 5.0 on 2024-02-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0008_tbl_scholarshipapply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_scholarshipapply',
            name='document',
            field=models.FileField(upload_to='Orgdoc/'),
        ),
    ]
