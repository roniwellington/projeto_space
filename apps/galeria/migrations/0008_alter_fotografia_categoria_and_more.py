# Generated by Django 5.0.6 on 2024-05-18 01:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galeria", "0007_fotografia_usuario_alter_fotografia_categoria"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fotografia",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("NEBULOSA", "Nebulosa"),
                    ("PLANETA", "Planeta"),
                    ("GALÁXIA", "Galáxia"),
                    ("ESTRELA", "Estrela"),
                ],
                default="",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="fotografia",
            name="publicada",
            field=models.BooleanField(default=True),
        ),
    ]
