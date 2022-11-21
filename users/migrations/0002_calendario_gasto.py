# Generated by Django 4.1.3 on 2022-11-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='calendario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('hecho', models.BooleanField(default=False)),
                ('crear', models.DateTimeField(auto_now_add=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]