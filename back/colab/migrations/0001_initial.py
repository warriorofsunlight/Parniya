# Generated by Django 5.0.3 on 2024-03-31 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11)),
                ('last_name', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cv', models.FileField(upload_to='cv/')),
                ('linkedin', models.URLField()),
            ],
        ),
    ]
