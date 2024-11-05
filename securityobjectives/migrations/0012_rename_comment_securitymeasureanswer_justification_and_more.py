# Generated by Django 5.1.2 on 2024-11-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("governanceplatform", "0030_scriptlogentry"),
        ("securityobjectives", "0011_alter_securityobjectivestatus_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="securitymeasureanswer",
            old_name="comment",
            new_name="justification",
        ),
        migrations.AddField(
            model_name="securitymeasureanswer",
            name="sectors",
            field=models.ManyToManyField(
                to="governanceplatform.sector", verbose_name="Sectors"
            ),
        ),
    ]