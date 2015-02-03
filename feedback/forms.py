#!/usr/bin/env python
from django import forms

from feedback.models import Feedback
from feedback.settings import DEFAULT_STATUS


class FeedbackForm(forms.ModelForm):
    '''The form shown when giving feedback'''

    class Meta:
        model = Feedback
        exclude = ('date_submitted', )
        widgets = {
            'url': forms.HiddenInput()
        }

    def clean_status(self):
        status = self.cleaned_data.get('status', '')
        if status == '' or status is None:
            return DEFAULT_STATUS
        return status
