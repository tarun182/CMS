# Generated by Django 2.1.7 on 2019-03-19 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_name', models.CharField(max_length=200)),
                ('Status', models.CharField(choices=[('Y', 'Free'), ('N', 'In use')], max_length=1)),
            ],
        ),
    ]
