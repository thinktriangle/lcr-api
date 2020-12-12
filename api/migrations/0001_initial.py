# Generated by Django 3.1.4 on 2020-12-12 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cr_id', models.IntegerField(unique=True)),
                ('source_url', models.CharField(max_length=255, unique=True)),
                ('registration_number', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('additional_name', models.CharField(max_length=255)),
                ('governorate', models.CharField(choices=[('BE', 'Beirut'), ('ML', 'Mount Lebanon'), ('NL', 'North Lebanon'), ('BA', 'Bekaa'), ('SL', 'South Lebanon'), ('NA', 'Nabatieh'), ('AK', 'Akkar'), ('BH', 'Baalbek-Hermel'), ('UK', 'Unknown')], default='UK', max_length=2)),
                ('registration_date', models.DateTimeField()),
                ('record_type', models.CharField(max_length=128)),
                ('company_status', models.CharField(max_length=128)),
                ('company_duration', models.CharField(max_length=128)),
                ('legal_form', models.CharField(max_length=128)),
                ('capital', models.DecimalField(decimal_places=2, max_digits=15)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('relationship', models.CharField(max_length=128)),
                ('stock', models.IntegerField()),
                ('quota', models.IntegerField()),
                ('ratio', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='api.company')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='api.person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]