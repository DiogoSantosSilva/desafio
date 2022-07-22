from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class BookRating(models.Model):
    book_id = models.IntegerField()
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
    )
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating ID:{self.id}"
