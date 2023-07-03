# Generated by Django 4.2 on 2023-04-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algapp', '0003_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='menu',
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_id', models.ManyToManyField(db_index=True, to='algapp.dishes')),
                ('restaurant_id', models.ManyToManyField(db_index=True, to='algapp.restaurant')),
            ],
        ),
    ]
