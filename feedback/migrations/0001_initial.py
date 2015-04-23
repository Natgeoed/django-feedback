# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(help_text='The URL from which the feedback was given.', max_length=255, verbose_name='url')),
                ('subject', models.CharField(default=b'', max_length=255, verbose_name='subject', blank=True, choices=[(b'suggestion', b'I have a suggestion'), (b'kudos', b'Kudos - I like something'), (b'error', b'Something went wrong'), (b'lost', b'I got stuck'), (b'missing', b"I can't find something")])),
                ('feedback', models.TextField(default=b'', verbose_name='feedback')),
                ('audience', models.CharField(default=b'', max_length=255, verbose_name='audience', blank=True, choices=[(b'educator', b'Educator'), (b'caregiver', b'Caregiver'), (b'student', b'Student')])),
                ('email', models.EmailField(default=b'', max_length=75, verbose_name='e-mail (optional)', blank=True)),
                ('status', models.CharField(default=b'unread', max_length=255, verbose_name='status', blank=True, choices=[(b'unread', b'Unread'), (b'exported', b'Exported'), (b'closed', b'Closed')])),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'feedback',
                'verbose_name_plural': 'feedback',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeedbackNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField()),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.ForeignKey(related_name='notes', to='feedback.Feedback')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
