# Generated by Django 5.1.3 on 2024-11-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vazifa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=256)),
                ('izoh', models.TextField()),
            ],
            options={
                'verbose_name': 'Vazifa',
                'verbose_name_plural': 'Vazifalar',
            },
        ),
        migrations.AlterModelOptions(
            name='kitob',
            options={'verbose_name': 'Kitob', 'verbose_name_plural': 'Kitoblar'},
        ),
    ]
