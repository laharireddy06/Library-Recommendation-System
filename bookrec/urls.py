from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("books/", views.books_page, name="books"),
    # path("all_books/", views.all_books, name="all_books"),  # <-- removed/commented
    path("contact/", views.contact, name="contact"),
    path("login/", views.login_view, name="login"),
    path("recommendations/", views.recommendations_page, name="recommendation"),

    # API
    path("api/books/", views.books_list, name="books_list"),
    path("api/recommend/", views.recommend_book, name="recommend_book"),
    path("check_book_exists/", views.check_book_exists, name="check_book_exists"),
    path("search-results/", views.search_results, name="search_results"),
    path("search-suggestions/", views.search_suggestions, name="search_suggestions"),
    path("recommend/", views.recommend_book, name="recommend_book"),
    path("get_recommendations/", views.recommend_book, name="get_recommendations"),
    path("book_list/", views.books_list, name="book_list"),

    # Chatbot
    path("chatbot/", views.chatbot_page, name="chatbot_page"),
    path("api/chatbot/", views.chatbot_api, name="chatbot_api"),

    # Admin
    path("admin/", admin.site.urls),
]
