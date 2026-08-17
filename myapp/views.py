from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from .models import *
from .forms import CardFormSet

# Create your views here.
def index(request):
    return render(request, "index.html")

def view_all_decks(request):
    all_decks = Deck.objects.all()
    return render(request, "all-decks.html", {"decks": all_decks})

def view_single_deck(request, deckid):
    single_deck = get_object_or_404(Deck, id=deckid)
    return render(request, "single-deck.html", {"deck":single_deck})

def edit_deck(request, deckid=None):
    deck = get_object_or_404(Deck, id=deckid) if deckid else Deck()
    if request.method == "POST":
        formset = CardFormSet(request.POST, instance=deck, prefix="cards")
        if formset.is_valid():
            deck.title = request.POST["title"]
            deck.description = request.POST["description"]
            deck.save()
            formset.instance = deck # Adds deck as a foreign key to card
            formset.save()
            return redirect("single-deck", deckid=deck.id)
    else:
        formset = CardFormSet(instance=deck, prefix="cards")
    return render(request, "edit-deck.html", {"deck": deck, "formset": formset})
            
