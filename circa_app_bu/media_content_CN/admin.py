from django.contrib import admin

  
from .models import Theme_CN, subtheme_I_CN, subtheme_V_CN, subtheme_A_CN, Image_CN, Video_CN, Audio_CN

admin.site.register(Theme_CN)

# Define the admin class
class MediaAdmin(admin.ModelAdmin):
    list_display = ('url', 'theme', 'subtheme', 'caption')
    fields = [('theme', 'subtheme'),'path','caption']

admin.site.register(subtheme_I_CN)
admin.site.register(subtheme_V_CN)
admin.site.register(subtheme_A_CN)
admin.site.register(Image_CN)
admin.site.register(Video_CN)
admin.site.register(Audio_CN)




# Register your models here.
