# Generated by Django 4.2.4 on 2023-08-13 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0002_admin_service_remove_user_address_customer_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mobile_no', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
            ],
        ),
        migrations.AlterField(
            model_name='admin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceApp.profile'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceApp.profile'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceApp.profile'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
