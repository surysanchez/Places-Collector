places = [
    {'name': 'Statue of Liberty', 'location': 'New York', 'description': 'One of the most iconic landmarks of NY.'},
    {'name': 'Grand Canyon' , 'location': 'Colorado', 'description': 'National Park natural attraction.'},
    {'name': 'Disney World', 'location': 'Florida', 'description': 'Entertainment resort park.' }
]


from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def places_index(request):
    return render(request, 'places/index.html', { 'places': places})