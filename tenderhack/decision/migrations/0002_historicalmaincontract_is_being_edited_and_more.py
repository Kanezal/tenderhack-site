# Generated by Django 4.2.7 on 2023-12-09 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("decision", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalmaincontract",
            name="is_being_edited",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicalmaincontract",
            name="last_edited_by",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="maincontract",
            name="is_being_edited",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="maincontract",
            name="last_edited_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
