from django.contrib import admin

from annalise_investors.models import InvestorUser, Pais, EstadosPais, Ciudad


class InvestorsUserAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apPaterno', 'apMaterno', 'telCasa', 'celular', 'colonia', 'calle',
                    'numExterior', 'ciudad', ]


admin.site.register(InvestorUser, InvestorsUserAdmin)
admin.site.register(Pais)
admin.site.register(EstadosPais)
admin.site.register(Ciudad)
