# Generated by Django 3.0.2 on 2020-11-21 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bincom', '0005_auto_20201121_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lga',
            name='lga_name',
            field=models.CharField(choices=[('ANIOCHA NORTH', 'ANIOCHA NORTH'), ('ANIOCH SOUTH', 'ANIOCH SOUTH'), ('ETHIOPE EAST', 'ETHIOPE EAST'), ('ETHIOPE WEST', 'ETHIOPE WEST'), ('IKA NORTH', 'IKA NORTH'), ('IKA SOUTH', 'IKA SOUTH'), ('ISOKO SOUTH', 'ISOKO SOUTH'), ('OSHIMILI NORTH', 'OSHIMILI NORTH'), ('OSHIMILI WEST', 'OSHIMILI WEST'), ('PATANI', 'PATANI'), ('SAPELE', 'SAPELE'), ('UGHELLI', 'UGHELLI'), ('UVWEI', 'UVWEI'), ('BODMADI', 'BODMADI'), ('WARRI NORTH', 'WARRI NORTH'), ('WARRI SOUTH', 'WARRI SOUTH')], default='WARRI SOUTH', max_length=50),
        ),
    ]