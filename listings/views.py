from django.views import generic
from .models import Listing
from django.shortcuts import render

def IndexView(request):
    listings = Listing.objects.all().order_by('date')
    return render(request, 'listings/index.html', {'all_listings': listings})


class DetailView(generic.DetailView):
    model = Listing
    template_name = 'listings/detail.html'