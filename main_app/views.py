
from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import ListView, DetailView
from .models import Place , Attraction
from .forms import ReviewForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def places_index(request):
    places = Place.objects.all()
    return render(request, 'places/index.html', {'places': places})

def places_detail(request, place_id):
    place = Place.objects.get(id=place_id)
    id_list = place.attractions.all().values_list('id')
    attractions_place_doesnt_have = Place.objects.exclude(id__in=id_list)
    review_form = ReviewForm()
    return render(request, 'places/detail.html', {'place': place, 'review_form': review_form, 'attractions': attractions_place_doesnt_have})

class PlaceCreate(CreateView):
    model = Place
    fields = ['name','location', 'description', 'yearBuilt']

class PlaceUpdate(UpdateView):
    model = Place
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['location', 'description', 'yearBuilt']


class PlaceDelete(DeleteView):
    model = Place
    success_url = '/places'


def add_review(request, place_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.place_id = place_id
        new_review.save()
        return redirect('places_detail', place_id=place_id)


class AttractionList(ListView):
    model = Attraction

class AttractionDetail(DetailView):
    model = Attraction

class AttractionCreate(CreateView):
    model = Attraction
    fields = '__all__'

class AttractionUpdate(UpdateView):
    model = Attraction
    fields = ['name', 'description']

class AttractionDelete(DeleteView):
    model = Attraction
    success_url = '/attractions'

def assoc_attraction(request, place_id, attraction_id):
    Place.objects.get(id=place_id).attractions.add(attraction_id)
    return redirect('places_detail', place_id=place_id)

def unassoc_attraction(request, place_id, attraction_id):
    Place.objects.get(id=place_id).attractions.remove(attraction_id)
    return redirect('places_detail', place_id=place_id)
