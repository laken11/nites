# Generated by Django 3.1 on 2020-09-12 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='address',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='booking',
        ),
        migrations.AddField(
            model_name='booking',
            name='passenger',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.RESTRICT, to='api.passenger'),
            preserve_default=False,
        ),
    ]
