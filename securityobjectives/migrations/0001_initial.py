# Generated by Django 4.2 on 2024-06-27 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.constraints
import django.db.models.deletion
import django.utils.timezone
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("governanceplatform", "0002_alter_company_country"),
    ]

    operations = [
        migrations.CreateModel(
            name="Domain",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="MaturityLevel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="SecurityMeasure",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.IntegerField(default=0)),
                (
                    "is_archived",
                    models.BooleanField(default=False, verbose_name="is archived"),
                ),
                (
                    "maturity_level",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="securityobjectives.maturitylevel",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Standard",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "regulation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="governanceplatform.regulation",
                    ),
                ),
                (
                    "regulator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="governanceplatform.regulator",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="StandardAnswer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "standard_notification_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "is_reviewed",
                    models.BooleanField(default=False, verbose_name="Reviewed"),
                ),
                (
                    "creator_name",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "creator_company_name",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                ("year_of_submission", models.PositiveIntegerField()),
                (
                    "standard",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="standard",
                        to="securityobjectives.standard",
                    ),
                ),
                (
                    "submitter_company",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="governanceplatform.company",
                    ),
                ),
                (
                    "submitter_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SecurityObejctive",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.IntegerField(default=0)),
                (
                    "unique_code",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "is_archived",
                    models.BooleanField(default=False, verbose_name="is archived"),
                ),
                (
                    "domain",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="domain",
                        to="securityobjectives.domain",
                    ),
                ),
                ("standards", models.ManyToManyField(to="securityobjectives.standard")),
            ],
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="SecurityMeasureTranslation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
                    ),
                ),
                ("description", models.TextField()),
                ("evidence", models.TextField()),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="securityobjectives.securitymeasure",
                    ),
                ),
            ],
            options={
                "verbose_name": "security measure Translation",
                "db_table": "securityobjectives_securitymeasure_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="SecurityMeasureAnswer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "security_measure_notification_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("comment", models.TextField()),
                (
                    "is_implemented",
                    models.BooleanField(default=False, verbose_name="Implemented"),
                ),
                ("review_comment", models.TextField()),
                (
                    "security_measure",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="security_measure",
                        to="securityobjectives.securitymeasure",
                    ),
                ),
                (
                    "standard_answer",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="standard_answer",
                        to="securityobjectives.standardanswer",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="securitymeasure",
            name="security_objective",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="securityobjectives.securityobejctive",
            ),
        ),
        migrations.CreateModel(
            name="MaturityLevelTranslation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="securityobjectives.maturitylevel",
                    ),
                ),
            ],
            options={
                "verbose_name": "maturity level Translation",
                "db_table": "securityobjectives_maturitylevel_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="DomainTranslation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="securityobjectives.domain",
                    ),
                ),
            ],
            options={
                "verbose_name": "domain Translation",
                "db_table": "securityobjectives_domain_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="StandardTranslation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                ("description", models.TextField()),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="securityobjectives.standard",
                    ),
                ),
            ],
            options={
                "verbose_name": "standard Translation",
                "db_table": "securityobjectives_standard_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="SecurityObejctiveTranslation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
                    ),
                ),
                (
                    "objective",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                ("description", models.TextField()),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="securityobjectives.securityobejctive",
                    ),
                ),
            ],
            options={
                "verbose_name": "security obejctive Translation",
                "db_table": "securityobjectives_securityobejctive_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.AddConstraint(
            model_name="securityobejctive",
            constraint=models.UniqueConstraint(
                deferrable=django.db.models.constraints.Deferrable["DEFERRED"],
                fields=("unique_code",),
                name="Unique_unique_code",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="securitymeasuretranslation",
            unique_together={("language_code", "master")},
        ),
        migrations.AlterUniqueTogether(
            name="maturityleveltranslation",
            unique_together={("language_code", "master")},
        ),
        migrations.AlterUniqueTogether(
            name="domaintranslation",
            unique_together={("language_code", "master")},
        ),
    ]
