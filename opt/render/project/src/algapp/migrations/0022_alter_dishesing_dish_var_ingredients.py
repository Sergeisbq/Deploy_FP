# Generated by Django 4.2 on 2023-07-02 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algapp', '0021_delete_allergens_delete_dishes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishesing',
            name='dish_var_ingredients',
            field=models.ManyToManyField(null=True, related_name='var_dishes', to='algapp.ingredients'),
        ),
    ]