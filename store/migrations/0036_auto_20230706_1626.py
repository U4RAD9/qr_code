# Generated by Django 3.1.3 on 2023-07-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0035_auto_20230706_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modalities',
            name='patientID',
            field=models.CharField(default=None, max_length=10),
        ),
    ]