# Generated by Django 3.2.5 on 2022-03-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_portfolio_sold_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='realized_profit',
            field=models.FloatField(default=0),
        ),
    ]
