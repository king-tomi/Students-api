# Generated by Django 3.2 on 2021-07-17 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('age', models.IntegerField()),
                ('discipline', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('registered', models.DateField(auto_now_add=True)),
                ('level', models.IntegerField(choices=[(100, 'first'), (200, 'second'), (300, 'third'), (400, 'fourth'), (500, 'fifth'), (600, 'sixth')])),
                ('matric', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('cgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('passport_photo', models.ImageField(upload_to='passports')),
            ],
        ),
    ]
