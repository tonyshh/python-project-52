# Generated by Django 4.1.7 on 2023-05-03 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Имя')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
