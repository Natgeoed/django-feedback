from django.template.loader import render_to_string
from django.views.generic import CreateView
from django.conf import settings
from django.core.mail import EmailMessage

from feedback.models import Feedback
from feedback.forms import FeedbackForm
from feedback.settings import ALERT_EMAIL, EMAIL_TEMPLATE


def send_email(to_list, subject, message, sender=settings.SERVER_EMAIL):
    msg = EmailMessage(subject, message, sender, to_list)
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'

    def get_initial(self):
        kwargs = super(FeedbackView, self).get_initial()
        if 'url' not in kwargs:
            referer = self.request.META.get('HTTP_REFERER', 'unknown')
            kwargs['url'] = self.request.GET.get('url', referer)
        return kwargs

    def get_success_url(self):
        if 'url' in self.kwargs:
            return self.kwargs['url']
        else:
            return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        super(FeedbackView, self).form_valid(form)
        if ALERT_EMAIL:
            d = form.cleaned_data
            try:
                send_email(
                    'Feedback received: {}'.format(d['subject']),
                    render_to_string(EMAIL_TEMPLATE, {'form': d}),
                    settings.SERVER_EMAIL,
                    [settings.FEEDBACK_EMAIL],
                    fail_silently=False,
                )
            except:
                pass
        form_class = self.get_form_class()
        self.initial = {'url': form.data.get('url')}
        blank_form = form_class(initial=self.get_initial())
        ctxt = self.get_context_data(form=blank_form, success=True)
        return self.render_to_response(ctxt)
