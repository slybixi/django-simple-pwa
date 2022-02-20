from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from pwa.defaults import get_app, get_pwa_config, get_service_worker

from teller_app.models import Index
from teller_app.models import Airdrop
from teller_app.models import Meta
from teller_app.models import Airdrop_Meta

# Create your views here.

def manifest_json(request):
	return JsonResponse(get_pwa_config())


def sw_js(request):
	return HttpResponse(get_service_worker() , content_type='application/javascript')


def app_js(request):
	return HttpResponse(get_app() , content_type='application/javascript')
	
def offline(request):
    home = Index.objects.all()
    meta = Meta.objects.all()
    airdrop = Airdrop.objects.all()
    airdrop_meta = Airdrop_Meta.objects.all()
    context = {
        'home': home,
        'meta': meta,
        'airdrop': airdrop,
        'airdrop_meta': airdrop_meta
    }
    
    return render(request, 'pwa/pwa_offline.html', context)
