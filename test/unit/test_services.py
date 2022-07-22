from books.services import RequestBookApi

request_book_api = RequestBookApi()


def test_sanitize() -> None:
    value = {
        "count": 1, "next": None, "previous": None,
        "results": [
            {
              "id": 1342,
              "title": "Pride and Prejudice",
              "authors": [
                {
                  "name": "Austen, Jane",
                  "birth_year": 1775,
                  "death_year": 1817
                }
              ],
              "translators": [],
              "subjects": [
                "Courtship -- Fiction",
                "Domestic fiction",
                "England -- Fiction",
                "Love stories",
                "Sisters -- Fiction",
                "Social classes -- Fiction",
                "Young women -- Fiction"
              ],
              "bookshelves": [
                "Best Books Ever Listings",
                "Harvard Classics"
              ],
              "languages": [
                "en"
              ],
              "copyright": False,
              "media_type": "Text",
              "formats": {
                "application/x-mobipocket-ebook": "https://www.gutenberg.org/ebooks/1342.kindle.images",
                "application/epub+zip": "https://www.gutenberg.org/ebooks/1342.epub.images",
                "application/rdf+xml": "https://www.gutenberg.org/ebooks/1342.rdf",
                "text/html; charset=utf-8": "https://www.gutenberg.org/files/1342/1342-h.zip",
                "text/plain; charset=utf-8": "https://www.gutenberg.org/files/1342/1342-0.zip",
                "image/jpeg": "https://www.gutenberg.org/cache/epub/1342/pg1342.cover.small.jpg",
                "text/html": "https://www.gutenberg.org/ebooks/1342.html.images"
              },
              "download_count": 34176
            }
        ]
    }

    response = request_book_api.sanitize(value)

    for book in response:
        assert "id" in book
        assert "title" in book
        assert "authors" in book
        assert "translators" not in book
        assert "subjects" not in book
        assert "bookshelves" not in book
        assert "languages" in book
        assert "copyright" not in book
        assert "media_type" not in book
        assert "formats" not in book
        assert "download_count" in book


def test_generate_query_param() -> None:
    expected_value = "?name=teste"
    value = {"name": "teste"}

    assert request_book_api.generate_query_param(value) == expected_value


def test_generate_multiples_query_param() -> None:
    expected_value = "?name=teste?search=Book Test"
    value = {"name": "teste", "search": "Book Test"}

    assert request_book_api.generate_query_param(value) == expected_value
