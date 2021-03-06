# Generated by Django 3.0.5 on 2020-05-19 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0012_auto_20200518_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidentlocation',
            old_name='latitude',
            new_name='location_lat',
        ),
        migrations.RenameField(
            model_name='incidentlocation',
            old_name='longitude',
            new_name='location_lng',
        ),
        migrations.AddField(
            model_name='incidentlocation',
            name='rating',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='incidentlocation',
            name='vicinity',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='incidentlocation',
            name='viewport_ne_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='incidentlocation',
            name='viewport_ne_lng',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='incidentlocation',
            name='viewport_sw_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='incidentlocation',
            name='viewport_sw_lng',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('reference', models.CharField(max_length=500)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='reporter.IncidentLocation')),
            ],
        ),
    ]
