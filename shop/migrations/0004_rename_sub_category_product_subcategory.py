# Generated by Django 5.0.1 on 2024-02-07 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_sybcategory_product_sub_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sub_category',
            new_name='subcategory',
        ),
    ]
