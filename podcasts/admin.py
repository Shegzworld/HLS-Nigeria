from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Podcaster, Podcast, Episode, Review, Subscription, Playlist

# Register your models here.
class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class SubscriptionInline(admin.TabularInline):
    model = Subscription
    extra = 1


class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title', 'description')
    inlines = [EpisodeInline, ReviewInline, SubscriptionInline]


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'podcast', 'published_at')
    search_fields = ('title', 'description')
    list_filter = ('podcast',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('podcast', 'user', 'rating')
    search_fields = ('podcast', 'user')
    list_filter = ('podcast', 'rating')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('podcast', 'user')
    search_fields = ('podcast', 'user')
    list_filter = ('podcast',)


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
    search_fields = ('user', 'title')
    filter_horizontal = ('episodes',)



admin.site.register(Podcaster)
admin.site.register(Podcast, PodcastAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Playlist, PlaylistAdmin)
