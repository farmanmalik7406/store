# Generated by Django 3.2.8 on 2021-10-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('created', models.DateField()),
            ],
        ),
    ]