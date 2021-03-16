from django.contrib import admin

from apps.waitlist.models import WaitlistEntry


# Register your models here.
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 
                    'created_at', 'updated_at',)
    list_filter = ('first_name', 'created_at')
    search_fields = ('first_name', 'last_name')


admin.site.register(WaitlistEntry, WaitlistAdmin)
