# Generated by Django 2.1.7 on 2019-03-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compo', '0004_auto_20190321_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Component_Type',
            field=models.CharField(blank=True, choices=[('Laptops', 'Laptops'), ('Storage', 'storage'), ('Mobiles', 'Mobiles'), ('Fashion', 'Fashion')], max_length=10),
        ),
        migrations.AlterField(
            model_name='items',
            name='Condition',
            field=models.CharField(blank=True, choices=[('USABLE', 'Usable'), ('FAULTY', 'faulty')], max_length=10),
        ),
        migrations.AlterField(
            model_name='items',
            name='Status',
            field=models.CharField(choices=[('FREE', 'Free'), ('IN USE', 'In use')], max_length=10),
        ),
    ]
