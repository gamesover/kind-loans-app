# Generated by Django 4.2.18 on 2025-02-05 11:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("loan", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="loanprofile",
            name="user",
            field=models.ForeignKey(
                help_text="The user associated with the loan profile.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="loan_profiles",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="contribution",
            name="borrower",
            field=models.ForeignKey(
                help_text="The borrower (loan profile) supported by this contribution.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contributions",
                to="loan.loanprofile",
            ),
        ),
        migrations.AddField(
            model_name="contribution",
            name="lender",
            field=models.ForeignKey(
                help_text="The lender (user) making this contribution.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contributions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
