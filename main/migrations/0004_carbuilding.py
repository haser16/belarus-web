# Generated by Django 3.2.12 on 2023-10-29 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_construction'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='carbuilding')),
            ],
        ),
    ]
