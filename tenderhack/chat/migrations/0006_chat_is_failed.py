# Generated by Django 4.2.7 on 2023-12-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0005_remove_chat_legacy_chat_is_closed_chat_main_form_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="chat",
            name="is_failed",
            field=models.BooleanField(default=False),
        ),
    ]
