from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views import View
from .models import Miasto, OfertaPracy
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.conf.urls.static import static

# Create your views here.
class SingleOfertaView(View):
    def get(self, request, pk):
        single_oferta = get_object_or_404(OfertaPracy, id=pk)
        oferty = OfertaPracy.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        context = {
            'single_oferta':single_oferta,
            'oferty':oferty,
        }
        return TemplateResponse(request, 'ogloszenie.html', context=context)

class OfertyView(View):
    def get(self, request):
        oferty_wszystkie = OfertaPracy.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        context = {
            'oferty_wszystkie':oferty_wszystkie,
        }
        return TemplateResponse(request, 'ogloszenia-wszystkie.html', context=context)
