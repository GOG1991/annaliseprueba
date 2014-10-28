from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from annalise import settings
from .models import entradas
from .forms import indexcontactform, ContacForm

import json


class inicioView(TemplateView):
    template_name = 'home.html'


class tiendasView(TemplateView):
    template_name = 'tiendas.html'


mensaje = ''


def index(request):
    banners = entradas.objects.filter(status= 'p').filter(categoria__slug='banners').order_by('-id')[:4]
    noticias = entradas.objects.filter(status= 'p').filter(categoria__slug='promociones').order_by('-id')[:3]
    if request.method == 'POST' and request.is_ajax():
        form = indexcontactform(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            comentario = form.cleaned_data['comentario']
            try:
                fullemail = nombre + " " + "<" + correo + ">"
                formulario = 'sugerencias'
                asunto = 'Comentario del sitio'
                enviodecorreo(asunto, comentario, fullemail, formulario)
                # status = 1
                mensaje = 'El correo se ha sido enviado correctamente'
                data = {
                    'status': 1,
                    'msj': mensaje,
                }
            except:
                # status = 2
                mensaje = 'Ha Ocurrido un problema al enviar el correo'
                data = {
                    'status': 1,
                    'msj': mensaje,
                }
        else:
            # status = 3
            mensaje = 'Error en el formulario'
            data = {
                'status': 3,
                'msj': mensaje,
            }

        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type="application/json")

    form = indexcontactform()
    template = 'home.html'
    return render_to_response(template, context_instance=RequestContext(request, locals()))


class entradasView(ListView):
    model = entradas

    def get_template_names(sef):
        return 'blog.html'


def news(request):
    news_list = entradas.objects.filter(status= 'p').filter(categoria__slug='noticias').order_by('-id')
    paginator = Paginator(news_list, 5)
    page = request.GET.get('page')
    news = paginador(page, paginator)
    template = 'blog.html'
    return render_to_response(template, context_instance=RequestContext(request, locals()))


def single(request, slug):
    single = get_object_or_404(entradas, slug=slug)
    template = 'single.html'
    return render_to_response(template, context_instance=RequestContext(request, locals()))


def promos(request):
    promociones_list = entradas.objects.filter(status= 'p').filter(categoria__slug='promociones').order_by('-id')
    paginator = Paginator(promociones_list, 5)
    page = request.GET.get('page')
    promociones = paginador(page, paginator)
    template = 'promociones.html'
    return render_to_response(template, context_instance=RequestContext(request, locals()))


def productsView(request):
    productos = entradas.objects.filter(categoria__id=settings.PRODUCTS)
    template = "productos.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))


var = ''


def paginador(page, paginator):
    try:
        var = paginator.page(page)
    except PageNotAnInteger:
        var = paginator.page(1)
    except EmptyPage:
        var = paginator.page(paginator.num_pages)
    return var


'''def contacto(request):
    if request.method == 'POST':
        form = ContacForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            try:
                fullemail = nombre + " " + "<" + correo + ">"
                formulario = 'contacto'
                enviodecorreo(asunto, mensaje, fullemail, formulario)
                status = 1
                mensaje = 'El correo se envio corectamente'
            except:
                status = 2
                mensaje = 'Ocurrio un problema al enviar el correo'
        else:
            status = 3
            mensaje = 'Error en el formulario'
    form = ContacForm()
    template = 'contacto.html'
    return render_to_response(template, context_instance=RequestContext(request, locals()))'''


def contacto(request):
    if request.method == 'POST' and request.is_ajax():
        form = ContacForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            try:
                fullemail = nombre + " " + "<" + correo + ">"
                formulario = 'contacto'
                enviodecorreo(asunto, mensaje, fullemail, formulario)
                # status = 1
                mensaje = 'El correo se envio corectamente gracias por contactarnos enseguida atenderemos tus comentarios'
                data = {
                    'status': 1,
                    'msj': mensaje,
                }
                # return HttpResponse(mensaje)
            except:
                # status = 2
                mensaje = 'Ocurrio un problema al enviar el correo'
                data = {
                    'status': 2,
                    'msj': mensaje,
                }
            json_data = json.dumps(data)
            return HttpResponse(json_data, content_type="application/json")

        else:
            # status = 3
            mensaje = 'Error en el formulario'
            data = {
                'status': 3,
                'msj': mensaje,
            }
            # return HttpResponse(mensaje)
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type="application/json")

    form = ContacForm()
    template = 'contacto.html'
    return render_to_response(template, context_instance=RequestContext(request, locals()))


def enviodecorreo(asunto, mensaje, de, formulario):
    para = 'info@super24.com.mx'
    asunto = asunto
    contenido = 'Correo enviado por: ' + de + "\n\n"
    contenido += 'Contenido del correo \n\n'
    contenido += mensaje + "\n\n"
    contenido += 'Desde el formulario de: ' + formulario + "\n\n"
    contenido += 'Para : ' + para + '\n'
    send_mail(asunto, contenido, de, [para])


def search(request):
    """Realizar consulta de busqueda de las paginas de palabras clave y de paginacion dado si los hay"""
    # Definiendo la cadena de consulta
    if request.method == 'GET':
        set_query = None
        query_build = None
        # Borro parametro page de la peticion GET
        params = request.GET.copy()
        if 'page' in params:
            print (params)
            del (params['page'])

        for field_name in params:
            value = request.GET.get('%s' % field_name)

            if value:
                query_build = (Q(titulo__icontains=value) | Q(contenido__icontains=value) | Q(
                    categoria__nombreCategoria__icontains=value))

                if set_query is None:
                    set_query = query_build
                else:
                    set_query = set_query & query_build

        if set_query:
            resultados_list = entradas.objects.filter(set_query).exclude(categoria__slug='banners').order_by('?')
            paginator = Paginator(resultados_list, 5)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                resultados = paginator.page(page)
            except (EmptyPage, InvalidPage):
                resultados = paginator.page(paginator.num_pages)

            path = params.urlencode()

            template = 'search.html'
    return render_to_response(template, context_instance=RequestContext(request, locals()))


def error404(request, template_name='404.html'):
    '''
    404 error handler
    '''

    return render_to_response(template_name, context_instance=RequestContext(request))


def error500(request, template_name='500.html'):
    '''
    500 error handler
    '''

    return render_to_response(template_name, context_instance=RequestContext(request))
