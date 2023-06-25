from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("profile/<str:name>", views.profile, name="profile"),
    path("category", views.category, name="category"),
    path("<int:drama_genre>",
         views.choose_category, name="choose_category"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist_drama/<int:drama_id>",
         views.watchlist_drama, name="watchlist_drama"),
    path("favorite", views.favorite, name="favorite"),
    path("favorite_action/<int:favdrama_id>",
         views.favorite_action, name="favorite_action"),
    path("<str:title>", views.drama, name="drama"),
    path("<str:title>/addreview", views.review, name="review"),
    path("<str:title>/<int:review_id>/deletereview",
         views.d_review, name="d_review"),
]
