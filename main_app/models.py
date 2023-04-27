from django.db import models

from django.urls import reverse
from datetime import date
# Create your models here.

# TYPES = (
#     ('E', 'Entertainment'),
#     ('H', 'Historic'),
#     ('M', 'Museums'),
#     ('P', 'Parks & Forests'),
#     ('C', 'Caves & Caverns'),
#     ('B', 'Bridges'),
#     ('G', 'Ghost Towns'),
#     ('L', 'Lakes'),
#     ('W', 'Waterfalls'),
#     ('M', 'Mountains'),
#     ('B', 'Beaches'),
#     ('O', 'Others')
# )

RATINGS = (
    ('E', 'Excellent'),
    ('F', 'Fair'), 
    ('B', 'Bad')
)

class Attraction(models.Model):
    name = models.CharField(max_length=60)
    # type = models.CharField(max_length=1, choices=TYPES, default=TYPES[0][0])
    description = models.TextField(max_length=250)

    # place = models.ForeignKey(Place, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
        # return f"{self.get_type_display()}"
    
    def get_absolute_url(self):
        return reverse('attractions_detail', kwargs={'pk': self.id})
    
  
    
class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    yearBuilt = models.IntegerField()
     # Add the M:M relationship
    attractions = models.ManyToManyField(Attraction)
    primary_key=True

    def review_for_today(self):
        return self.review_set.filter(date=date.today()).count() >= 1

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    
    def get_absolute_url(self):
        return reverse('places_detail', kwargs={'place_id': self.id})
    

class Review(models.Model):
    
    date = models.DateField('review date')
    rating = models.CharField(max_length=1, choices=RATINGS, default=RATINGS[0][0]) 

    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"  
    
    class Meta:
        ordering = ['-date'] 

     