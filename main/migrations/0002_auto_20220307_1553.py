# Generated by Django 3.2.9 on 2022-03-07 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyWH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(default=0, verbose_name="Ishlashi kerak bo'lgan soatlar")),
                ('current', models.FloatField(default=0, verbose_name='Ishlagan soati')),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=150, verbose_name='Familiya')),
                ('name', models.CharField(max_length=150, verbose_name='Ism')),
            ],
            options={
                'verbose_name': 'Ishchi',
                'verbose_name_plural': 'Ishchilar',
            },
        ),
        migrations.DeleteModel(
            name='UserAccount',
        ),
        migrations.AddField(
            model_name='dailywh',
            name='date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.date'),
        ),
        migrations.AddField(
            model_name='dailywh',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.employee'),
        ),
    ]