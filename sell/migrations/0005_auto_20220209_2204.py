# Generated by Django 3.1.7 on 2022-02-09 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0004_auto_20220209_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='sell.link'),
        ),
    ]
