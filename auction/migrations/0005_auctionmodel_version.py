# Generated by Django 2.2.5 on 2019-09-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_auctionmodel_bidders'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionmodel',
            name='version',
            field=models.IntegerField(default=0),
        ),
    ]
