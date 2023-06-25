from django.contrib import admin
from .models import User, Drama, Region, Actor, Category, Favorite, Watchlist, Upcoming, Review

# Register your models here.


class ActorAdmin(admin.ModelAdmin):
    list_display = ('first', "last", 'role')
    filter_horizontal = ('drama',)
    search_fields = ('first',)


class DramaAdmin(admin.ModelAdmin):
    list_display = ('user', "title", 'genre',
                    'region', 'total_episode', 'img_small', 'year', 'date')
    filter_horizontal = ('category',)


class RegionAdmin(admin.ModelAdmin):
    display = 'region'


class CategoryAdmin(admin.ModelAdmin):
    display = 'category'


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('favdrama', "username")


class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('drama', "username")


admin.site.register(User)
admin.site.register(Drama, DramaAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(Upcoming)
admin.site.register(Review)
