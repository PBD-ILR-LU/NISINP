# Generated by Django 4.2 on 2024-03-12 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "governanceplatform",
            "0010_cert_certuser_user_certs_certuser_unique_certuser",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="regulatoruser",
            name="sectors",
            field=models.ManyToManyField(blank=True, to="governanceplatform.sector"),
        ),
        migrations.AlterField(
            model_name="sectorcompanycontact",
            name="sector",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="governanceplatform.sector",
            ),
        ),
    ]