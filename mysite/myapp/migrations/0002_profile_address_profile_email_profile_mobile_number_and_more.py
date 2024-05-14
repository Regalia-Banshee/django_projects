# Generated by Django 5.0.6 on 2024-05-14 01:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="address",
            field=models.TextField(default="Unknown"),
        ),
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.EmailField(default="Unknown", max_length=320),
        ),
        migrations.AddField(
            model_name="profile",
            name="mobile_number",
            field=models.CharField(default="Unknown", max_length=255),
        ),
        migrations.AlterField(
            model_name="profile",
            name="name",
            field=models.CharField(default="Unknown", max_length=255),
        ),
    ]
