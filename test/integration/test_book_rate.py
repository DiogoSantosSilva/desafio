import json
import pytest
from rest_framework import status


def test_get_all_book_rating(client, book_fixture) -> None:
    response = client.get("/books/rate/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1


@pytest.mark.django_db
def test_post_book_rating(client) -> None:
    payload = {
        "bookId": 1050,
        "rating": 5,
        "review": "test post"
    }
    response = client.post(
        f"/books/rate/",
        data=json.dumps(payload),
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_get_book_rating_by_id(client, book_fixture) -> None:
    book_rate = book_fixture
    response = client.get(f"/books/rate/{book_rate.id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["bookId"] == book_rate.book_id
    assert data["rating"] == book_rate.rating
    assert data["review"] == book_rate.review


@pytest.mark.django_db
def test_error_to_get_book_rating_by_id(client) -> None:
    response = client.get(f"/books/rate/15555")
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_put_book_rating_by_id(client, book_fixture) -> None:
    book_rate = book_fixture

    payload = {
        "bookId": 5050,
        "rating": 4,
        "review": "test update"
    }
    response = client.put(
        f"/books/rate/{book_rate.id}",
        data=json.dumps(payload),
        content_type='application/json'
    )
    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert data["bookId"] == payload["bookId"]
    assert data["rating"] == payload["rating"]
    assert data["review"] == payload["review"]


@pytest.mark.django_db
def test_delete_book_rating_by_id(client, book_fixture) -> None:
    book_rate = book_fixture
    response = client.delete(f"/books/rate/{book_rate.id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT
