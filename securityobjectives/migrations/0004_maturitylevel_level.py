# Generated by Django 5.1.2 on 2024-10-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("securityobjectives", "0003_remove_standardanswer_is_finished_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="maturitylevel",
            name="level",
            field=models.IntegerField(default=0),
        ),
    ]