# Generated by Django 4.1.3 on 2022-12-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
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
                ("userId", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                ("passwd", models.CharField(max_length=50)),
                ("gender", models.CharField(max_length=10)),
                ("hobby", models.CharField(max_length=50)),
                ("job", models.CharField(max_length=50)),
                ("reg_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]