# Generated by Django 4.2 on 2023-04-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algapp', '0004_remove_restaurant_menu_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
    ]
