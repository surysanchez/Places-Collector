from django.db import models

from django.urls import reverse
# Create your models here.

RATINGS = (
    ('E', 'Excellent'),
    ('F', 'Fair'), 
    ('B', 'Bad')
)

class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    yearBuilt = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'place_id': self.id})
    

class Review(models.Model):
    date = models.DateField('review date')
    rating = models.CharField(max_length=1, choices=RATINGS, default=RATINGS[0][0]) 

    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"   

     