from django.contrib import admin
from feedback.models import Feedback, FeedbackNote


def export_and_update(modeladmin, request, queryset):
    from django.http import HttpResponse
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
    data = queryset.values_list('url', 'subject', 'feedback', 'email', 'date_submitted', 'status')
    output = StringIO()

    # Header
    output.write('"url","subject","feedback","email","date submitted","status"\n')
    for row in data:
        output.write('"{0}","{1}","{2}","{3}","{4:%Y-%m-%d %H:%M:%S}","{5}"\n'.format(*row))
    queryset.update(status='exported')
    response = HttpResponse(output.getvalue(), content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="feedback_export.csv"'
    output.close()
    return response
export_and_update.short_description = "Export selected feedback and change status"


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
    actions = (export_and_update, )

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
