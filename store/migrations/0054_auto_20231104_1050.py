# Generated by Django 3.1.3 on 2023-11-04 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0053_auto_20231102_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modalities',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.users'),
        ),
    ]