# Generated by Django 4.1.3 on 2022-12-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post2",
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
                ("subject", models.CharField(max_length=50)),
                ("content", models.TextField()),
                ("writer", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=50)),
                ("reg_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
