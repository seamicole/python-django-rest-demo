# Generated by Django 3.1.1 on 2021-09-14 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("location", "0002_populate_locations"),
    ]

    operations = [
        migrations.CreateModel(
            name="Currency",
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
                ("name", models.CharField(max_length=255)),
                ("name_plural", models.CharField(max_length=255)),
                ("code", models.CharField(max_length=10, unique=True)),
                (
                    "number",
                    models.PositiveIntegerField(blank=True, null=True, unique=True),
                ),
                ("symbol", models.CharField(max_length=10)),
                ("symbol_native", models.CharField(max_length=20)),
                (
                    "in_usd",
                    models.DecimalField(
                        blank=True, decimal_places=15, max_digits=30, null=True
                    ),
                ),
                (
                    "per_usd",
                    models.DecimalField(
                        blank=True, decimal_places=15, max_digits=30, null=True
                    ),
                ),
                ("rates_updated_at", models.DateTimeField(blank=True, null=True)),
                (
                    "flag",
                    models.ImageField(
                        blank=True, null=True, upload_to="currency/currency/flag"
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="currencies",
                        to="location.country",
                    ),
                ),
            ],
            options={
                "verbose_name": "Currency",
                "verbose_name_plural": "Currencies",
            },
        ),
    ]
