# Generated by Django 4.2 on 2023-04-29 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('algapp', '0002_dishes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('address', models.CharField(db_index=True, max_length=100)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='algapp.dishes')),
            ],
        ),
    ]