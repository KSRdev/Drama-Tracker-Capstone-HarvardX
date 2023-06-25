# Create your models here.
from calendar import c
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='tracker/static/tracker/img/avatar', default="tracker/static/tracker/img/avatar/default.jpg", null=True, blank=True)

    def __str__(self):
        return f"{self.username}"


class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"


class Region(models.Model):
    region = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.region}"


class Drama(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user")
    title = models.CharField(max_length=64)
    description = models.TextField()
    genre = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="genres", blank=True, default=None)
    category = models.ManyToManyField(
        Category, blank=True, related_name="categories")
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="select_region", default=None)
    total_episode = models.IntegerField()
    link_trailer = models.URLField(blank=True)
    img_cover = models.ImageField(
        upload_to='tracker/static/tracker/img/cover', default=None, blank=True)
    img_small = models.ImageField(
        upload_to='tracker/static/tracker/img/small', default=None, blank=True)
    year = models.IntegerField()
    date = models.DateTimeField(
        editable=False,  default=timezone.now)

    def __str__(self):
        return f"{self.title}"


class Actor(models.Model):
    first = models.CharField(max_length=64)
    middle = models.CharField(max_length=64, blank=True)
    last = models.CharField(max_length=64)
    profile = models.URLField(max_length=200, blank=True)
    role = models.CharField(max_length=64, blank=True)
    drama = models.ManyToManyField(
        Drama, blank=True, related_name="actors")
    nationality = models.ForeignKey(
        Region, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first} {self.middle} {self.last} {self.drama}"


class Watchlist(models.Model):
    drama = models.ForeignKey(Drama, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=64, null=True)

    def __str__(self):
        return f"{self.drama}"


class Favorite(models.Model):
    favdrama = models.ForeignKey(Drama, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=64, null=True)

    def __str__(self):
        return f"{self.favdrama} "


class Upcoming(models.Model):
    d_title = models.CharField(max_length=64, null=True)
    d_link_img = models.URLField(blank=True)
    d_total_episode = models.IntegerField()
    d_region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="d_select_region", default=None)
    d_date = models.DateTimeField(
        editable=False,  default=timezone.now)

    def __str__(self):
        return f"{self.d_title} "


class Review(models.Model):
    drama_name = models.CharField(null=True, max_length=64)
    ratings = models.IntegerField(null=True)
    username = models.CharField(max_length=64, null=True)
    review = models.TextField(null=True)
    r_date = models.DateTimeField(
        editable=False, default=timezone.now)

    def __str__(self):
        return f"{self.drama_name} "
