from django.contrib import admin
from .models import Question, Choice
# Register your models here.

#change site header
admin.site.site_header = "Polls Admin"
admin.site.title = "Polls Admin Area"
admin.site.title = "Welcome to the Polls admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pup_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


# To register you db entities to the admin functionality
# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
