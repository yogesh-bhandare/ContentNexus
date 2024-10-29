# Generated by Django 4.2.16 on 2024-10-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='_status',
            field=models.CharField(blank=True, choices=[('publish', 'Publish'), ('pending', 'Pending'), ('draft', 'Draft'), ('on_hold', 'On Hold')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('publish', 'Publish'), ('pending', 'Pending'), ('draft', 'Draft'), ('on_hold', 'On Hold')], default='draft', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='status_changed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]