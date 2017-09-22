from django.shortcuts import render
from .models import Cubelist
from django.template import loader
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

def index(request):
    all_cards = Cubelist.objects.all()
    template = loader.get_template('cards/index.html')
    query = request.GET.get("q")
    if query:
        try:
            int(query)
            all_cards = all_cards.filter(card_cost__icontains=query)
        except ValueError:
            all_cards = all_cards.filter(card_name__icontains=query)
    #info for template
    count = (all_cards.count())
    context = {'all_cards':all_cards, 'count': count}

    return HttpResponse(template.render(context,request))

class CardCreate(CreateView):
    model = Cubelist
    fields = ['card_name', 'card_cost', 'card_image']

class CardUpdate(UpdateView):
    model = Cubelist
    fields = ['card_name', 'card_cost', 'card_image']

