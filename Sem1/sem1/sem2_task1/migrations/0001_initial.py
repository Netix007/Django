# Generated by Django 4.2.3 on 2023-08-01 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoinPlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(max_length=10)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]