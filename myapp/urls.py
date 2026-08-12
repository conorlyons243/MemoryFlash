from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("decks", views.view_all_decks, name="all-decks"),
    path("decks/<int:deckid>", views.view_single_deck, name="single-deck"),
    
]
