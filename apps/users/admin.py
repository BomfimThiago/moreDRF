from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.users.models import User, UserProfile


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'is_admin', 'is_student')
    list_filter = ('is_admin', 'is_student')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_student')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_student'),
        }),
    )

    search_fields = ('email', 'is_student')
    ordering = ('email',)
    filter_horizontal = ()


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)