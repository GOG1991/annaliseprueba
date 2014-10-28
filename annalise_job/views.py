from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.forms.models import inlineformset_factory as inline 

from datetime import datetime

from .models import applicants, vacancies, aplicant_vacancie
from .forms import applicantForm, aplicantVacancieForm
from annalise_cms.views import paginador


def dataApplicant(request, id):
    vacancie = get_object_or_404(vacancies, id = id)
    aplicante = applicants()
    aplicanteFormset = inline(applicants, aplicant_vacancie, extra = 1, can_delete = False, form = aplicantVacancieForm)
    aplicanteform = applicantForm()
    aplFormset = aplicanteFormset()

    if request.method == 'POST':
        print('entra a post')
        aplicanteform = applicantForm(request.POST, request.FILES)
        print('entra a recibir datos')
        if aplicanteform.is_valid():
            print('form valido')
            aplicante = aplicanteform.save(commit = False)
            aplFormset = aplicanteFormset(request.POST, instance = aplicante)
            if aplFormset.is_valid():
                print('segundo form valido')
                aplicante.save()
                human = True
                obj = aplFormset.save(commit = False)
                aplFormset.save()
                #return HttpResponseRedirect('/')
                return HttpResponseRedirect('/ok/')
            else:
                pass
        else:
            print('no es valido')
            pass
            
    template = 'aplicante.html'
    return render_to_response(template, context_instance=RequestContext(request, locals()))


def vacanciesList(request):
    #obtengo todas las vacantes disponibles
    vacancies_list = vacancies.objects.filter(visible = True)
    paginator = Paginator(vacancies_list, 5)
    page = request.GET.get('page')
    vacantes = paginador(page, paginator)
    template = 'jobs.html'
    return render_to_response(template, context_instance=RequestContext(request, locals()))


def vacancie_single(request, slug):
    #presento la vacante para que se pueda aplicar a esta.
    vacancie = get_object_or_404(vacancies, slug = slug)
    template = 'vacancie.html'
    return render_to_response(template, context_instance=RequestContext(request, locals()))
