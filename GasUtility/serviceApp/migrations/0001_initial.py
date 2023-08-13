# Generated by Django 4.2.4 on 2023-08-13 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('mobile_no', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(verbose_name='created date')),
                ('updated_at', models.DateTimeField(verbose_name='update date')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='created date')),
                ('updated_at', models.DateTimeField(verbose_name='update date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceApp.user')),
            ],
        ),
    ]
