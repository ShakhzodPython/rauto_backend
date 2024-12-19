# Generated by Django 5.0.5 on 2024-12-11 12:21

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Body type',
                'verbose_name_plural': 'Body types',
            },
        ),
        migrations.CreateModel(
            name='CarCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='Gearbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Gearbox',
                'verbose_name_plural': 'Gearboxes',
            },
        ),
        migrations.CreateModel(
            name='MachineCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Machine condition',
                'verbose_name_plural': 'Machine conditions',
            },
        ),
        migrations.CreateModel(
            name='MachineDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Machine drive',
                'verbose_name_plural': 'Machine drives',
            },
        ),
        migrations.CreateModel(
            name='TypeFuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Type fuel',
                'verbose_name_plural': 'Type fuels',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('desc', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('currency', models.CharField(choices=[('som', 'SOM'), ('usd', 'USD')], max_length=5, verbose_name='Currency')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('mileage', models.IntegerField(verbose_name='Mileage')),
                ('engine', models.CharField(max_length=5, verbose_name='Engine')),
                ('location', models.CharField(choices=[('tashkent', 'Tashkent'), ('samarkand', 'Samarkand')], max_length=50, verbose_name='Location')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('body_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_body_type', to='products.bodytype', verbose_name='Body type')),
                ('images', models.ManyToManyField(to='media.media', verbose_name='Images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='products.carcategory', verbose_name='category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_color', to='products.color', verbose_name='Color')),
                ('gearbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_gearbox', to='products.gearbox', verbose_name='Gearbox')),
                ('machine_condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_machine_condition', to='products.machinecondition', verbose_name='Machine condition')),
                ('machine_drive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_machine_drive', to='products.machinedrive', verbose_name='Machine drive')),
                ('type_fuel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_type_fuel', to='products.typefuel', verbose_name='Type fuel')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
