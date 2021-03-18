from django.contrib import admin

from apps.lectures.models import Lecture


# Register your models here.
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ('-date',)


admin.site.register(Lecture, LectureAdmin)
