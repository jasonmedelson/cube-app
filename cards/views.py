from django.contrib.auth import authenticate,login
from django.shortcuts import render
from .models import Cubelist
from django.template import loader
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
import random

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

def pack(request):
    all_cards = Cubelist.objects.all()
    count = (all_cards.count())
    card_set = []
    count = (all_cards.count())
    for num in range(15):
        card = all_cards.get(card_id__exact=random.randint(0,count-1))
        card_set.append(card)
    template = loader.get_template('cards/index.html')
    context = {'all_cards':card_set, 'count': count}
    return HttpResponse(template.render(context, request))

class CardCreate(CreateView):
    model = Cubelist
    fields = ['card_name', 'card_cost', 'card_image']

class CardUpdate(UpdateView):
    model = Cubelist
    fields = ['card_name', 'card_cost', 'card_image']

def loginView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        # Return an 'invalid login' error message.
        return HttpResponse.Redirect("/login")

