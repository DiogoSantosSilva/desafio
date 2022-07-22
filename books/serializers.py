from books.models import BookRating
from rest_framework import serializers


class BookRatingSerializer(serializers.ModelSerializer):
    bookId = serializers.IntegerField(source="book_id")

    class Meta:
        model = BookRating
        fields = ["bookId", "rating", "review"]
