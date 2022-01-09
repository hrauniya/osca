# Generated by Django 4.0 on 2022-01-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_allergies_allergy_rename_coops_coop_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='missed_jobes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='preferred_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
