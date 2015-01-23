from django.db import models
from django.utils.translation import ugettext_lazy as _

from .settings import SUBJECT_CHOICES, STATUS_CHOICES, DEFAULT_STATUS


class Feedback(models.Model):
    url = models.CharField(
        max_length=255,
        verbose_name=_('url'),
        help_text=_('The URL from which the feedback was given.'))
    subject = models.CharField(
        _('subject'),
        choices=SUBJECT_CHOICES,
        max_length=255,
        blank=True,
        default='')
    feedback = models.TextField(
        _('feedback'),
        default='')
    email = models.EmailField(
        _('e-mail (optional)'),
        blank=True,
        default='')
    status = models.CharField(
        _('status'),
        choices=STATUS_CHOICES,
        max_length=255,
        blank=True,
        default=DEFAULT_STATUS)
    date_submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('feedback')
        verbose_name_plural = _('feedback')

    def __unicode__(self):
        return u'Feedback on {url}'.format(url=self.url)


class FeedbackNote(models.Model):
    """
    A note on a piece of feedback
    """
    feedback = models.ForeignKey('feedback.Feedback', related_name="notes")
    user = models.ForeignKey('auth.User')
    note = models.TextField()
    date_submitted = models.DateTimeField(blank=True, auto_now_add=True)
