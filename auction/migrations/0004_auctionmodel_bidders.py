# Generated by Django 2.2.5 on 2019-09-25 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auto_20190925_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionmodel',
            name='bidders',
            field=models.TextField(default='[]'),
        ),
    ]
