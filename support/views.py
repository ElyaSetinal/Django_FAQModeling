from django.shortcuts import get_object_or_404, render

from django.views.generic import ListView
from .models import Faq


# Create your views here.

class NList(ListView):
    model = Faq
    template_name = 'support/normal.html'

class AList(ListView):
    model = Faq
    template_name = 'support/account.html'

class EList(ListView):
    model = Faq
    template_name = 'support/etc.html'

def index(request):
    return render(request, 'index.html')

def detail_view(request, object_id):
    details = get_object_or_404(Faq, id = object_id)
    return render(request, 'detail_view.html', {'detail':details})