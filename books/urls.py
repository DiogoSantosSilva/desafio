from django.urls import path
from books import views

urlpatterns = [
    path("", views.get_book_by_title),
    path("<int:book_id>/detail", views.BookDetailView.as_view()),
    path("rate/", views.ListBookRatingView.as_view()),
    path("rate/<int:id>", views.BookRatingView.as_view()),
]
