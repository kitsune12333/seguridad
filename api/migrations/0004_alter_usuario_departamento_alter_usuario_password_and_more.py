# Generated by Django 4.2 on 2024-06-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='departamento',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(unique=True),
        ),
    ]