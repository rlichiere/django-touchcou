# Generated by Django 2.0.5 on 2018-05-11 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(default='WAITING_REGISTRATIONS_OPENING', max_length=200)),
                ('genre', models.CharField(default='HF', max_length=2)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(related_name='games', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
