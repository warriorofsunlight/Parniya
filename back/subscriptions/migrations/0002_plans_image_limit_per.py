# Generated by Django 5.0.3 on 2024-04-02 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='image_limit_per',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
