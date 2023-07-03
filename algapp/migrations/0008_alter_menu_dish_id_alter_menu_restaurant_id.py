# Generated by Django 4.2 on 2023-04-30 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algapp', '0007_alter_customer_allergens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='dish_id',
            field=models.ManyToManyField(blank=True, db_index=True, to='algapp.dishes'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='restaurant_id',
            field=models.ManyToManyField(blank=True, db_index=True, to='algapp.restaurant'),
        ),
    ]
