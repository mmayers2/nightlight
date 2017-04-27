from django.db import models

class Listing(models.Model):
    artist = models.CharField(max_length=250)
    venue = models.CharField(max_length=250)
    date = models.DateTimeField(max_length=250)
    ROCK='RO'
    HIPHOP='HH'
    POP='POP'
    EDM='EDM'
    NA='NA'
    GENRES = (
        (ROCK, 'Rock'),
        (HIPHOP, 'Hip Hop'),
        (POP, 'Pop'),
        (EDM, 'Electronic'),
        (NA, 'N/A')
    )
    genre = models.CharField(max_length=3, choices=GENRES, default=NA)

    def __str__(self):
        self.date = str(self.date)
        return self.artist + ' - ' + self.date
