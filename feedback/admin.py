from django.contrib import admin
from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('url', 'subject', 'date_submitted')
    list_filter = ('subject', )
    date_hierarchy = 'date_submitted'
    ordering = ('-date_submitted', )
    search_fields = ('feedback', 'email', 'url')

admin.site.register(Feedback, FeedbackAdmin)

# vim: et sw=4 sts=4
