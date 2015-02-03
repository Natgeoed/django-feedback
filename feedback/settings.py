from django.conf import settings

DEFAULT_SETTINGS = {
    'ALERT_EMAIL': [],
    'EMAIL_TEMPLATE': 'feedback/email.html',
    'SUBJECT_CHOICES': (
        ("suggestion", "I have a suggestion"),
        ("kudos", "Kudos - I like something"),
        ("error", "Something went wrong"),
        ("lost", "I got stuck"),
        ("missing", "I can't find something"),
    ),
    'STATUS_CHOICES': (
        ('unread', 'Unread'),
        ('exported', 'Exported'),
        ('closed', 'Closed'),
    ),
    'AUDIENCE_CHOICES': (
        ('educator', 'Educator'),
        ('caregiver', 'Caregiver'),
        ('student', 'Student'),
    ),
    'DEFAULT_STATUS': 'unread',
}

USER_SETTINGS = DEFAULT_SETTINGS.copy()
USER_SETTINGS.update(getattr(settings, 'FEEDBACK_SETTINGS', {}))

if not isinstance(USER_SETTINGS['ALERT_EMAIL'], (list, tuple)):
    USER_SETTINGS['ALERT_EMAIL'] = [USER_SETTINGS['ALERT_EMAIL']]

globals().update(USER_SETTINGS)
