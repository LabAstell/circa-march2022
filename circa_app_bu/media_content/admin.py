from django.contrib import admin

from .models import Theme, subtheme_I, subtheme_V, subtheme_A, Image, Video, Audio

admin.site.register(Theme)

# Define the admin class
class MediaAdmin(admin.ModelAdmin):
    list_display = ('url', 'theme', 'subtheme', 'caption')
    fields = [('theme', 'subtheme'),'path','caption']

admin.site.register(subtheme_I)
admin.site.register(subtheme_V)
admin.site.register(subtheme_A)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Audio)
