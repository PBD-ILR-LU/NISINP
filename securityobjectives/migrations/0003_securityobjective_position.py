# Generated by Django 5.1.2 on 2024-10-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "securityobjectives",
            "0002_remove_securitymeasuretranslation_evidence_evidence_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="securityobjective",
            name="position",
            field=models.IntegerField(default=0),
        ),
    ]
