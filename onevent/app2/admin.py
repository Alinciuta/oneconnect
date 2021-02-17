from django.contrib import admin

# Register your models here.

from app2.models import Question

class questionsAdmin(admin.ModelAdmin):
        list_display=['name', 'email', 'body']
admin.site.register(Question,questionsAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'eveniment', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_questions']

    def approve_questions(self, request, queryset):
        queryset.update(active=True)
