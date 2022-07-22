import logging
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import views
from books.serializers import BookRatingSerializer
from books.models import BookRating
from books.services import RequestBookApi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from drf_yasg import openapi

title = openapi.Parameter('test', openapi.IN_QUERY, description="Book title", type=openapi.TYPE_STRING)


@swagger_auto_schema(method='get', manual_parameters=[title])
@api_view(["GET"])
def get_book_by_title(request):
    """
    Get book by title
    """
    title_param = request.query_params.get("title")
    if not title_param:
        return Response(
            "Title query parameter is required!", status=status.HTTP_400_BAD_REQUEST
        )

    api_book = RequestBookApi()
    if not api_book:
        return Response(status=status.HTTP_204_NO_CONTENT)
    response = api_book.get(search=title_param)
    return Response(response, status=status.HTTP_200_OK)


# Create your views here.
class BookRatingView(views.APIView):
    def get(self, request, id) -> Response:
        """
        Return a book rating by id
        """
        try:
            book_rate = BookRating.objects.get(id=id)
            serializer = BookRatingSerializer(book_rate, many=False)
            return Response(serializer.data)
        except BookRating.DoesNotExist as error:
            logging.error(f"{error}")
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id: int) -> Response:
        """
            Update a book rating by id
        """
        try:
            book_rate = BookRating.objects.get(id=id)
            serializer = BookRatingSerializer(instance=book_rate, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BookRating.DoesNotExist as error:
            logging.error(f"{error}")
            return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, id: int) -> Response:
        try:
            book_rate = BookRating.objects.get(id=id)
            book_rate.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except BookRating.DoesNotExist as error:
            logging.error(f"{error}")
            return Response(status=status.HTTP_204_NO_CONTENT)


class ListBookRatingView(views.APIView):
    def post(self, request) -> Response:
        """
        Create a book rating
        """
        try:
            serializer = BookRatingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as error:
            logging.error(f"{error}")
            raise error

    def get(self, request) -> Response:
        """
         Get all books rating
        """
        try:
            books = BookRating.objects.all()
            serializer = BookRatingSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BookRating.DoesNotExist as error:
            logging.error(f"{error}")
            return Response(status=status.HTTP_204_NO_CONTENT)


class BookDetailView(views.APIView):

    def get(self, request, book_id: int) -> Response:
        """
        Get a book by id from a third party and merge with the book
        rate from database
        """
        api_book = RequestBookApi()
        books = api_book.get(ids=book_id)["books"]
        if not books:
            return Response(status=status.HTTP_204_NO_CONTENT)

        rating = self.get_book_rating_by_book_id(book_id)

        book = books[0]
        book.update(rating)
        return Response(book, status=status.HTTP_200_OK)

    def get_book_rating_by_book_id(self, book_id: int) -> dict:
        """
        Get the books rating
        """
        try:
            books = BookRating.objects.filter(book_id=book_id).all()
            rating = 0
            reviews = []

            for book in books:
                rating += book.rating
                reviews.append(book.review)

            average = rating / len(books) if len(books) > 0 else rating

            return {"rating": average, "reviews": reviews}
        except BookRating.DoesNotExist as error:
            logging.error(f"{error}")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            logging.error(f"{error}")
            raise error
