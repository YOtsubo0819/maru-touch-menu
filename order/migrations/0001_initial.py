# Generated by Django 3.2.6 on 2021-08-18 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname_kana', models.CharField(max_length=50)),
                ('fullname_kanji', models.CharField(max_length=50)),
                ('birthday', models.DateTimeField()),
                ('gender', models.CharField(max_length=5)),
                ('patientid', models.IntegerField(blank=True, null=True)),
                ('tel_number', models.CharField(max_length=13)),
                ('postal_code', models.CharField(max_length=8)),
                ('address1', models.CharField(blank=True, max_length=100, null=True)),
                ('insurer_id', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('price', models.IntegerField()),
                ('code', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('type', models.CharField(max_length=10)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.patient')),
            ],
        ),
    ]
