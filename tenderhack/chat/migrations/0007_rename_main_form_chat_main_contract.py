# Generated by Django 4.2.7 on 2023-12-09 12:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0006_chat_is_failed"),
    ]

    operations = [
        migrations.RenameField(
            model_name="chat",
            old_name="main_form",
            new_name="main_contract",
        ),
    ]
