# Generated by Django 5.0 on 2024-02-11 02:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_tbl_medicalshop'),
        ('Helpers', '0007_initial'),
        ('Organization', '0005_delete_tbl_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('book_address', models.CharField(max_length=50)),
                ('book_contact', models.CharField(max_length=50)),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_organization')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Helpers.tbl_post')),
            ],
        ),
    ]
