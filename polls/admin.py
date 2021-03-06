from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    admin.site.register(Question)
    admin.site.register(Choice)
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # model = Choice
    # extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]

# admin.site.register(Question, QuestionAdmin)

#todo: add bootstrap, deploy to heroku