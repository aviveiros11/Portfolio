from django.shortcuts import render
from projects.models import Quote
import sqlite3

# Create your views here.
def index(request):

    quotes = Quote.objects.all()
    context = {
        'quotes': quotes
    }
    return render(request, 'index.html', context)

