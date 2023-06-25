from turtle import title
from django.shortcuts import render
from .models import User, Drama, Category, Watchlist, Favorite, Upcoming, Review
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.


def index(request):

    list_dramas = Drama.objects.filter().order_by(
        '-date')
    upcoming_dramas = Upcoming.objects.filter().order_by(
        '-d_date')
    drama_list = generate_watch_drama(request)
    favorite_drama_list = generate_favorite_drama(request)

    paginator = Paginator(list_dramas, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "tracker/index.html", {
        "list_dramas": page_obj,
        "upcoming_dramas": upcoming_dramas,
        "drama_list": drama_list,
        "favorite_drama_list": favorite_drama_list
    })


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "tracker/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                username, email, password, last_name=last_name, first_name=first_name)
            user.save()
        except IntegrityError:
            return render("register", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "tracker/register.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "tracker/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "tracker/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def profile(request, name):
    user = User.objects.get(username=name)

    if request.method == "POST":
        u = User.objects.get(username=name)
        u.delete()
        return HttpResponseRedirect(reverse("index"))

    return render(request, "tracker/profile.html", {
        "user": user
    })


def category(request):
    list_dramas = Drama.objects.order_by('title').all()
    categories = Category.objects.all()
    drama_list = generate_watch_drama(request)
    favorite_drama_list = generate_favorite_drama(request)
    paginator = Paginator(list_dramas, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "tracker/category.html", {
        "list_dramas": page_obj,
        "categories": categories,
        "drama_list": drama_list,
        "favorite_drama_list": favorite_drama_list
    })


def choose_category(request, drama_genre):
    list_dramas = Drama.objects.filter(category=drama_genre).all()
    genre = Category.objects.filter(id=drama_genre)
    drama_list = generate_watch_drama(request)
    favorite_drama_list = generate_favorite_drama(request)

    categories = Category.objects.all()
    paginator = Paginator(list_dramas, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "tracker/category.html", {
        "title": drama_genre,
        "list_dramas": page_obj,
        "categories": categories,
        "genres": genre,
        "drama_list": drama_list,
        "favorite_drama_list": favorite_drama_list
    })


def drama(request, title):
    drama = Drama.objects.get(title=title)
    drama_list = generate_watch_drama(request)
    favorite_drama_list = generate_favorite_drama(request)
    review = Review.objects.filter(drama_name=title).all()
    return render(request, "tracker/drama.html", {
        "drama": drama,
        "actors": drama.actors.all(),
        "categories": drama.category.all(),
        "title": title,
        "drama_list": drama_list,
        "reviews": review,
        "favorite_drama_list": favorite_drama_list
    })


def watchlist(request):

    watch_lists = Watchlist.objects.filter(
        username=request.user.username).all()
    list_dramas = Drama.objects.all()
    drama_list = generate_watch_drama(request)
    favorite_drama_list = generate_favorite_drama(request)
    paginator = Paginator(watch_lists, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "tracker/watchlist.html", {
        "watch_list": page_obj,
        "list_dramas": list_dramas,
        "drama_list": drama_list,
        "favorite_drama_list": favorite_drama_list
    })


def watchlist_drama(request, drama_id):
    condition = request.POST.get("condition")
    origin = request.POST.get("origin")

    if condition == "add":
        drama = Drama.objects.get(id=drama_id)
        save = Watchlist(drama=drama, username=request.user.username)
        save.save()
        if origin == "drama":
            return HttpResponseRedirect(reverse("watchlist"))
        elif origin == "index":
            return HttpResponseRedirect(reverse('index'))
        elif origin == "watchlist":
            return HttpResponseRedirect(reverse('watchlist'))
    elif condition == "remove":
        drama = Drama.objects.get(id=drama_id)
        remove = Watchlist.objects.get(
            drama=drama, username=request.user.username)
        remove.delete()

        if origin == "drama":
            return HttpResponseRedirect(reverse("watchlist"))
        elif origin == "index":
            return HttpResponseRedirect(reverse('index'))
        elif origin == "watchlist":
            return HttpResponseRedirect(reverse('watchlist'))


def generate_watch_drama(request):
    watched_list = Watchlist.objects.filter(
        username=request.user.username).all()
    drama_list = []
    for drama in watched_list:
        drama_list.append(drama.drama)
    return drama_list


def favorite(request):

    favorite_lists = Favorite.objects.filter(
        username=request.user.username).all()
    list_dramas = Drama.objects.all()
    favorite_drama_list = generate_favorite_drama(request)
    paginator = Paginator(favorite_lists, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "tracker/favorite.html", {
        "favorite_lists": page_obj,
        "list_dramas": list_dramas,
        "favorite_drama_list": favorite_drama_list
    })


def favorite_action(request, favdrama_id):
    condition = request.POST.get("fav")
    origin = request.POST.get("favv")

    if condition == "favorite":
        favdrama = Drama.objects.get(id=favdrama_id)
        save = Favorite(favdrama=favdrama, username=request.user.username)
        save.save()
        if origin == "drama":
            return HttpResponseRedirect(reverse("favorite"))
        elif origin == "index":
            return HttpResponseRedirect(reverse('index'))
        elif origin == "favorite":
            return HttpResponseRedirect(reverse('favorite'))
    elif condition == "unfavorite":
        favdrama = Drama.objects.get(id=favdrama_id)
        remove = Favorite.objects.get(
            favdrama=favdrama, username=request.user.username)
        remove.delete()

        if origin == "drama":
            return HttpResponseRedirect(reverse("favorite"))
        elif origin == "index":
            return HttpResponseRedirect(reverse('index'))
        elif origin == "favorite":
            return HttpResponseRedirect(reverse('favorite'))


def generate_favorite_drama(request):
    favorite_list_list = Favorite.objects.filter(
        username=request.user.username).all()
    favorite_drama_list = []
    for favorite in favorite_list_list:
        favorite_drama_list.append(favorite.favdrama)
    return favorite_drama_list


def review(request, title):
    review = request.POST.get("review")
    rating = request.POST.get("rating")
    username = request.user.username
    review = Review(username=username,
                    drama_name=title, review=review, ratings=rating)
    review.save()

    return HttpResponseRedirect(reverse("drama", args=(title,)))


def d_review(request, review_id, title):
    if request.method == "POST":
        review_id = Review.objects.get(id=review_id)
        review_id.delete()
        return HttpResponseRedirect(reverse("drama", args=(title,)))
