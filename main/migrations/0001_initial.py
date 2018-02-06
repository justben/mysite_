# Generated by Django 2.0.1 on 2018-02-06 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dmline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dmlines', models.CharField(max_length=10)),
                ('y1', models.FloatField()),
                ('x1', models.FloatField()),
                ('y2', models.FloatField()),
                ('x2', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10)),
                ('file', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=10)),
                ('y', models.FloatField()),
                ('x', models.FloatField()),
                ('h', models.FloatField()),
                ('num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Number')),
            ],
        ),
        migrations.AddField(
            model_name='dmline',
            name='num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Number'),
        ),
    ]