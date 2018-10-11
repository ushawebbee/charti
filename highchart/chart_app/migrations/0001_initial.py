# Generated by Django 2.0.3 on 2018-10-07 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
