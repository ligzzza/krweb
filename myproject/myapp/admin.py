from django.contrib import admin
from .models import geeхам, User

class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam_date', 'is_public', 'created_at')
    search_fields = ('name', 'participants__email')
    list_filter = ('is_public', 'created_at', 'exam_date')
    filter_horizontal = ('participants',)

admin.site.register(geeхам)
admin.site.register(User)