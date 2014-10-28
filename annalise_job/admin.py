from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import applicants, vacancies, aplicant_vacancie

class vancancie_aplicantInline(admin.TabularInline):
	model = aplicant_vacancie
	extra = 0
	readonly_fields = ('date',)
	verbose_name = _('Aplicante')
	verbose_name_plural = _('Aplicantes')

class applicantAdmin(admin.ModelAdmin):
	list_display = ('name', 'last_name','gender','email',)
	search_fields = ('name', 'email',)
	inlines = [vancancie_aplicantInline,]


class vancancieAdmin(admin.ModelAdmin):
	list_display = ('title','published','visible',)
	readonly_fields = ('published',)
	list_filter = ('visible',)
	search_fields = ('title',)
	prepopulated_fields = {"slug": ("title",)}
	inlines = [vancancie_aplicantInline,]

admin.site.register(applicants, applicantAdmin)
admin.site.register(vacancies, vancancieAdmin)
#admin.site.register(aplicant_vacancie)
