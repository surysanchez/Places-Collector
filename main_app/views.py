
from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView 

from .models import Place
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
    review_form = ReviewForm()
    return render(request, 'places/detail.html', {'place': place, 'review_form': review_form})

def add_review(request, place_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.place_id = place_id
        new_review.save()
        return redirect('detail', place_id=place_id)

class PlaceCreate(CreateView):
    model = Place
    fields = '__all__'
      # Special string pattern Django will use
    # success_url = '/places/{place_id}' 
    # # <--- must specify an exact ID
    # Or..more fitting... you want to just redirect to the index page
    # success_url = '/places'

class PlaceUpdate(UpdateView):
    model = Place
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['location', 'description', 'yearBuilt']


class PlaceDelete(DeleteView):
    model = Place
    success_url = '/places'