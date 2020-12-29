# Generated by Django 3.1.4 on 2020-12-24 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import userProfile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_id', models.IntegerField(default=1, verbose_name='Question At')),
                ('score', models.IntegerField(default=0)),
                ('data', models.TextField(default='<2020-12-26T12:00:00.0+05:30,0>')),
                ('correct', models.IntegerField(default=0)),
                ('total_ques', models.IntegerField(default=userProfile.models.Profile.num_ques, verbose_name='Total Questions')),
                ('winner', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-score'],
            },
        ),
    ]
