# Generated by Django 3.0.5 on 2020-05-04 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsapi', '0002_auto_20200504_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='testsapi.Member'),
        ),
        migrations.AlterField(
            model_name='member',
            name='idno',
            field=models.CharField(default='XGXFZ168K', max_length=9, unique=True),
        ),
    ]