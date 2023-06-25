# Generated by Django 4.1 on 2022-10-10 08:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0024_upcoming'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcoming',
            name='d_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='upcoming',
            name='d_title',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
