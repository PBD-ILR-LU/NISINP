# Generated by Django 5.1.1 on 2024-10-10 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("incidents", "0018_incident_regulator"),
    ]

    operations = [
        migrations.AddField(
            model_name="predefinedanswer",
            name="position",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="predefinedanswer",
            name="question",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="incidents.question",
                verbose_name="Question",
            ),
        ),
    ]
