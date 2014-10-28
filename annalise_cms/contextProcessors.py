from django.contrib.flatpages.models import FlatPage

from annalise import settings

def menu(request):
	menu = FlatPage.objects.exclude(id__in= settings.EXCLUDEMENU ).order_by('id')
	return {'menu':menu,}