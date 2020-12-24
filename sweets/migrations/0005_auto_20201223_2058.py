# Generated by Django 3.1.4 on 2020-12-23 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sweets', '0004_auto_20201221_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bags',
            name='scoops',
        ),
        migrations.AddField(
            model_name='bags',
            name='scoops',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sweets.scoops'),
        ),
    ]