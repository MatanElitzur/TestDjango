from django.contrib import admin
from polls.models import Question
from polls.models import Choice

#class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 3
    
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)

# Register your models here.
