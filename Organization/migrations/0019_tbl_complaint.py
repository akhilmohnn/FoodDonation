# Generated by Django 5.0 on 2024-04-11 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_tbl_adminlogin'),
        ('Guest', '0004_tbl_medicalshop'),
        ('Organization', '0018_delete_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complainttitle', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
                ('complaintdate', models.DateField(auto_now_add=True)),
                ('complainttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_comptype')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_organization')),
            ],
        ),
    ]