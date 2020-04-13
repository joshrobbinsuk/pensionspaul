# Generated by Django 3.0.5 on 2020-04-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0005_auto_20200408_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='band_1_lower',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='fund',
            name='band_1_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='fund',
            name='band_2_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='fund',
            name='band_3_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='fund',
            name='band_4_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='fund',
            name='band_5_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='fund',
            name='band_6_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='fund',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fund',
            name='end_1_band_2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='fund',
            name='end_2_band_3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='fund',
            name='end_3_band_4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='fund',
            name='end_4_band_5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='fund',
            name='end_5_band_6',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='fund',
            name='fixed_costs_ongoing',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='fund',
            name='fixed_costs_year_start',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='fund',
            name='fund_type',
            field=models.CharField(choices=[('p', 'Pension Company'), ('f', 'Fund Supermarket')], default='p', max_length=1),
        ),
        migrations.AlterField(
            model_name='fund',
            name='platform_type',
            field=models.CharField(choices=[('itb', 'ITB'), ('wf', 'WF')], default='itb', max_length=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='setup_costs',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]