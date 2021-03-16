from django.contrib import admin

from apps.certificates.models import Certificate


# Register your models here.
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Certificate, CertificateAdmin)
