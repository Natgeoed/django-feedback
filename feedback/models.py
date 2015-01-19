from django.db import models
from django.utils.translation import ugettext_lazy as _

from .settings import SUBJECT_CHOICES


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
        default=''
    )
    feedback = models.TextField(
        _('feedback'),
        default='')
    email = models.EmailField(
        _('e-mail (optional)'),
        blank=True,
        default='')
    date_submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('feedback')
        verbose_name_plural = _('feedback')

    def __unicode__(self):
        return u'Feedback on {url}'.format(url=self.url)
