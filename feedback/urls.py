from django.conf.urls import url

from .views import FeedbackView


urlpatterns = [
    url(r'^$', FeedbackView.as_view(), name='feedback_submit'),
    ]

# vim: et sw=4 sts=4
