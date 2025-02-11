# Generated by Django 4.2.18 on 2025-02-11 05:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loan", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name="contribution",
            name="borrower",
            field=models.ForeignKey(
                help_text="The borrower (loan profile) that will be supported.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contributions",
                to="loan.loanprofile",
            ),
        ),
        migrations.AlterField(
            model_name="repayment",
            name="is_applied",
            field=models.BooleanField(
                default=False,
                help_text="True if the repayment has been paid out to contributors.",
            ),
        ),
        migrations.AddField(
            model_name="loanprofile",
            name="categories",
            field=models.ManyToManyField(
                related_name="loan_profiles", to="loan.category"
            ),
        ),
    ]
