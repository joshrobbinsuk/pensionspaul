# Generated by Django 3.0.5 on 2020-04-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fund",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "brand",
                    models.CharField(help_text="enter brand name", max_length=100),
                ),
                (
                    "setup_costs",
                    models.IntegerField(help_text="enter yr 1 set-up  costs"),
                ),
                (
                    "fixed_costs_year_start",
                    models.IntegerField(
                        help_text="enter fixed costs applied at year start"
                    ),
                ),
                (
                    "fixed_costs_ongoing",
                    models.IntegerField(
                        help_text="enter fixed costs applied throughout year"
                    ),
                ),
                (
                    "band_1_lower",
                    models.IntegerField(help_text="enter lower end of band one"),
                ),
                (
                    "band_1_upper",
                    models.IntegerField(help_text="enter upper end of band one"),
                ),
                ("band_1_rate", models.IntegerField(help_text="enter band one rate")),
            ],
        ),
    ]
