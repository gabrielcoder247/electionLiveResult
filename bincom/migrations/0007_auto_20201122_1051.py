# Generated by Django 3.0.2 on 2020-11-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bincom', '0006_auto_20201121_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lga',
            name='lga_name',
            field=models.CharField(max_length=50),
        ),
    ]
