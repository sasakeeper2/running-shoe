# Generated by Django 5.2 on 2025-04-06 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='runningshoe',
            name='best_for',
            field=models.CharField(default='easy days', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='runningshoe',
            name='heel_to_toe_drop',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='runningshoe',
            name='stack_height',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
    ]
