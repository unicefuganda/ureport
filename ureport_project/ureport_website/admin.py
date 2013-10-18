from django.contrib import admin
from .models import Partners, Read, Watch, Quotes


class PartnersAdmin(admin.ModelAdmin):
# fields display on change list
    list_display = ['title', 'created']
# fields to filter the change list with
    list_filter = ['published', 'created']
# fields to search in change list
    search_fields = ['title', 'description', 'content']
# enable the date drill down on change list
    date_hierarchy = 'created'
# enable the save buttons on top on change form
    save_on_top = True
# prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}


class ReadAdmin(admin.ModelAdmin):
# fields display on change list
    list_display = ['title', 'created']
# fields to filter the change list with
    list_filter = ['published', 'created']
# fields to search in change list
    search_fields = ['title', 'content']
# enable the date drill down on change list
    date_hierarchy = 'created'
# enable the save buttons on top on change form
    save_on_top = True
# prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}


class WatchAdmin(admin.ModelAdmin):
# fields display on change list
    list_display = ['title', 'created']
# fields to filter the change list with
    list_filter = ['published', 'created']
# fields to search in change list
    search_fields = ['title', 'content']
# enable the date drill down on change list
    date_hierarchy = 'created'
# enable the save buttons on top on change form
    save_on_top = True
# prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}


class QuotesAdmin(admin.ModelAdmin):
# fields display on change list
    list_display = ['question', 'author', 'created']
# fields to filter the change list with
    list_filter = ['published', 'created']
# fields to search in change list
    search_fields = ['author', 'content']
# enable the date drill down on change list
    date_hierarchy = 'created'
# enable the save buttons on top on change form
    save_on_top = True


admin.site.register(Partners, PartnersAdmin)
admin.site.register(Watch, WatchAdmin)
admin.site.register(Read, ReadAdmin)
admin.site.register(Quotes, QuotesAdmin)
