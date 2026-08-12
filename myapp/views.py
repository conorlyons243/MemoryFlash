from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def view_all_decks(request):
    all_decks = Deck.objects.all()
    return render(request, "all-decks.html", {"decks": all_decks})

def view_single_deck(request, deckid):
    single_deck = get_object_or_404(Deck, id=deckid)
    return render(request, "single-deck.html", {"deck":single_deck})
