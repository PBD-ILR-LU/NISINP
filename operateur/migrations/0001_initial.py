# Generated by Django 4.2 on 2023-05-03 11:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operateur_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('operateur_identifier', models.CharField(max_length=64)),
                ('operateur_name', models.CharField(max_length=64)),
                ('operateur_country', models.CharField(max_length=64)),
                ('operateur_adress', models.CharField(max_length=255)),
                ('operateur_email', models.CharField(blank=True, max_length=100, null=True)),
                ('operateur_phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('operateur_monarc_path', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OperateurUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('user_email', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=255)),
                ('user_lastname', models.CharField(max_length=64)),
                ('user_firstname', models.CharField(max_length=64)),
                ('user_phone_number', models.CharField(max_length=30)),
                ('entity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operateur.operateur')),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
    ]
