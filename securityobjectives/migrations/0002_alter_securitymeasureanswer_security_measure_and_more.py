# Generated by Django 5.1.2 on 2024-10-22 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("securityobjectives", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="securitymeasureanswer",
            name="security_measure",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="securitymeasureanswers",
                to="securityobjectives.securitymeasure",
            ),
        ),
        migrations.AlterField(
            model_name="securitymeasureanswer",
            name="standard_answer",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="securitymeasureanswers",
                to="securityobjectives.standardanswer",
            ),
        ),
    ]