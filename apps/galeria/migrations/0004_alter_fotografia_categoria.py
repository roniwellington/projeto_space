# Generated by Django 5.0.6 on 2024-05-11 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada_alter_fotografia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('ESTRELA', 'Estrela'), ('PLANETA', 'Planeta'), ('GALÁXIA', 'Galáxia'), ('NEBULOSA', 'Nebulosa')], default='', max_length=100),
        ),
    ]
