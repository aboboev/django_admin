from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    class Media:
        js = ('admin/js/admin/DateTimeShortcuts.js',)


admin.site.register(Question, QuestionAdmin)
