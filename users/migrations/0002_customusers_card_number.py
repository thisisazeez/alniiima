# Generated by Django 3.2.4 on 2021-07-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusers',
            name='card_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]