from django.contrib import admin

from .models import Faq, Inquiry, Answer

# Register your models here.

@admin.register(Faq)
class Faqmodeladmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'question', 'created_person',
    'created_time', 'last_modify_person', 'last_modified_time')
    list_p_page = 20
    readonly_fields = ('created_time', 'last_modified_time')

class AnswerInline(admin.StackedInline):
    model = Answer
    max_num = 3
    verbose_name = '답변'

@admin.register(Inquiry)
class Inqmodeladmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'writer', 'emailAddress', 'email_allow','phonenumber','sms_allow', 'created_time',)
    list_p_page = 20
    inlines = [AnswerInline]