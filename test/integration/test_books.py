from rest_framework import status


def test_get_book(client) -> None:
    response = client.get("/books/?title=Pride and Prejudice")
    assert response.status_code == status.HTTP_200_OK


def test_book_details_body(client) -> None:
    response = client.get("/books/?title=Pride and Prejudice")
    books = response.json()["books"]
    for book in books:
        assert "id" in book
        assert "title" in book
        assert "authors" in book
        assert "languages" in book
        assert "download_count" in book


def test_get_book_without_title_param(client):
    response = client.get("/books/")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_book_detaild_by_id(client, book_fixture) -> None:
    book_id = 1342
    response = client.get(f"/books/{book_id}/detail")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == book_id
    assert "title"
    assert "authors" in data
    assert "download_count"
    assert "languages" in data
    assert "rating" in data
    assert "reviews" in data
