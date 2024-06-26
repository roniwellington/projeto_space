# Generated by Django 5.0.6 on 2024-05-12 01:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0006_alter_fotografia_categoria_alter_fotografia_foto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('PLANETA', 'Planeta'), ('ESTRELA', 'Estrela'), ('NEBULOSA', 'Nebulosa'), ('GALÁXIA', 'Galáxia')], default='', max_length=100),
        ),
    ]
