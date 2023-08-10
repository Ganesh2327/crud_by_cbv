# Generated by Django 4.2.1 on 2023-08-07 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SchoolName', models.CharField(max_length=100)),
                ('SchoolPrincpal', models.CharField(max_length=100)),
                ('SchoolLocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=100)),
                ('Sage', models.IntegerField()),
                ('SchoolName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Students', to='app.school')),
            ],
        ),
    ]
