from django.contrib import admin
from .models import questions, choice



# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_test']}),
        ('Date information', {'fields': ['date'],'classes':'collapse'}),
    ]
    inlines = [ChoiceInline]
    # list_display = ('question_test', 'date')
    list_display = ('question_test', 'date', 'was_published_recently')
    list_filter = ['date']
    search_fields = ['question_test']

admin.site.register(questions, QuestionAdmin)
admin.site.register(choice)
# admin.site.register(questions)
print("admin")