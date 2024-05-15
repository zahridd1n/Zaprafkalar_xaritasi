# Generated by Django 5.0.6 on 2024-05-15 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_zaprafka_lan_alter_zaprafka_lat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zaprafka',
            name='category',
        ),
        migrations.CreateModel(
            name='ZaprafkaCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('zaprafka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.zaprafka')),
            ],
        ),
    ]
