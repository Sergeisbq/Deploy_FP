# Generated by Django 4.2 on 2023-06-28 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algapp', '0020_alter_customer_allergens'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Allergens',
        ),
        migrations.DeleteModel(
            name='Dishes',
        ),
    ]
