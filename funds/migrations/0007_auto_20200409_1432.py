# Generated by Django 3.0.5 on 2020-04-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("funds", "0006_auto_20200408_1540"),
    ]

    operations = [
        migrations.RemoveField(model_name="fund", name="end_3_band_4",),
        migrations.AddField(
            model_name="fund",
            name="end_ç3_band_4",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
    ]
