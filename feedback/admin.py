from django.contrib import admin
from feedback.models import Feedback, FeedbackNote


class FeedbackNoteInline(admin.TabularInline):
    model = FeedbackNote
    extra = 0


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('url', 'subject', 'date_submitted', 'status', 'extended_fields')
    list_filter = ('subject', 'status', )
    list_editable = ('status', )
    date_hierarchy = 'date_submitted'
    ordering = ('-date_submitted', )
    search_fields = ('feedback', 'email', 'url')
    inlines = (FeedbackNoteInline, )

    def extended_fields(self, obj):
        return """<div class="arrow" data-target="#extended-%(id)s">
        </div></td></tr>
        <tr class="extended" id="extended-%(id)s" style="display: none">
        <td colspan="6">%(feedback)s""" % ({
            'id': obj.id,
            'feedback': obj.feedback
        })
    extended_fields.allow_tags = True
    extended_fields.short_description = 'More'

admin.site.register(Feedback, FeedbackAdmin)

# vim: et sw=4 sts=4
