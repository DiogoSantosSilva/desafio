import pytest
from books.models import BookRating


@pytest.fixture
@pytest.mark.django_db
def book_fixture(db) -> BookRating:
    book_rating = BookRating(
        book_id=1342, rating=4, review="fixture"
    )
    book_rating.save()
    return book_rating
