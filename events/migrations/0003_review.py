# Generated by Django 4.0.2 on 2022-03-19 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_attending'),
        ('events', '0002_rename_datetime_event_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('text', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='events.event')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='accounts.userprofile')),
            ],
        ),
    ]
