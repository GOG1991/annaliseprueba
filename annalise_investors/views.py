from django.shortcuts import  render_to_response, HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from annalise_investors.forms import InvestorsUserForm


def investorsView(request):
    form = InvestorsUserForm()
    if request.method == 'POST':
        form = InvestorsUserForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/ok/')
            return HttpResponse('solicitud enviada , en breve nos pondremos en contacto contigo')
    template = "investors.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))


def ok(request):
    template = "ok.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))