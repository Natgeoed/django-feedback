from django.db import models
from django.utils.translation import ugettext_lazy as _

from .settings import (SUBJECT_CHOICES, STATUS_CHOICES, DEFAULT_STATUS,
                       AUDIENCE_CHOICES)


class Feedback(models.Model):
    url = models.CharField(
        verbose_name=_('url'), max_length=255,
        help_text=_('The URL from which the feedback was given.'))
    subject = models.CharField(
        verbose_name=_('subject'), max_length=255, blank=True,
        choices=SUBJECT_CHOICES, default='')
    feedback = models.TextField(
        verbose_name=_('feedback'), default='')
    audience = models.CharField(
        verbose_name=_('audience'), max_length=255, blank=True, default='',
        choices=AUDIENCE_CHOICES)
    email = models.EmailField(
        verbose_name=_('Email (optional)'), blank=True, default='')
    status = models.CharField(
        verbose_name=_('status'), choices=STATUS_CHOICES, max_length=255,
        blank=True, default=DEFAULT_STATUS)
    date_submitted = models.DateTimeField(
        auto_now_add=True)

    class Meta:
        verbose_name = _('feedback')
        verbose_name_plural = _('feedback')

    def __unicode__(self):
        return 'Feedback on {url}'.format(url=self.url)


class FeedbackNote(models.Model):
    """
    A note on a piece of feedback
    """
    feedback = models.ForeignKey('feedback.Feedback', related_name="notes")
    user = models.ForeignKey('auth.User')
    note = models.TextField()
    date_submitted = models.DateTimeField(blank=True, auto_now_add=True)
