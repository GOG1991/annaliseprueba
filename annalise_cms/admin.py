from django.contrib import admin
from .models import blogs, autores, entradas, categorias
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

from .forms import CategoryForm, EntadasForm

class PageForm(FlatpageForm):
    class Meta:
        model = FlatPage
        widgets = {
            'content': TinyMCE(attrs={'cols': 180, 'rows': 15}),
        }


class PageAdmin(FlatPageAdmin):
    form = PageForm


class categoriasAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ('nombreCategoria','usuario')
    prepopulated_fields = {"slug": ("nombreCategoria",)}
    readonly_fields = ('usuario',)
    def save_model(self, request, obj, form, change):
        if change:
            print ('Change es ', change)
        else:
            print('Change es ', change)
            obj.usuario = request.user
        obj.save()


class entradaAdmin(admin.ModelAdmin):
    form = EntadasForm
    readonly_fields = ('pubDate','modDate', 'usuario',)
    list_display = ('titulo', 'pubDate', 'status', 'usuario')
    #fields = ['titulo', 'slug', 'contenido', 'categoria', 'pubDate', 'modDate','usuario', 'status', 'imgDestacada']
    prepopulated_fields = {"slug": ("titulo",)}
    filter_horizontal = ('categoria',)
    fieldsets = ((
        None, {
            'fields': ('titulo','slug','contenido','categoria','status','imgDestacada')
        }),(
    'Otra informacion', {
        'fields': ('modDate',),
        'classes': ('collapse',)
        })
    )

    def save_model(self, request,obj,form,change):
        if change:
            print ('Change es ', change)            
        else:
            obj.usuario = request.user
        obj.save()


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
admin.site.register(blogs)
admin.site.register(autores)
admin.site.register(entradas, entradaAdmin)
admin.site.register(categorias, categoriasAdmin)

