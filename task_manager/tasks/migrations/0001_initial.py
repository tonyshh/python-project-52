# Generated by Django 4.2.9 on 2024-02-05 08:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TaskLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labels.label')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
