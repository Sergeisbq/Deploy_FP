# Generated by Django 4.2 on 2023-06-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algapp', '0019_alter_menu_dish_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='allergens',
            field=models.ManyToManyField(to='algapp.ingredients'),
        ),
    ]