# Generated by Django 4.2.7 on 2023-12-04 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0002_initial"),
        ("chat", "0003_formmessage_chat"),
    ]

    operations = [
        migrations.AddField(
            model_name="chat",
            name="legacy",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="market.proposal",
            ),
        ),
    ]
