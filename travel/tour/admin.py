from django.contrib import admin
from .models import *

# Register your models here.


class Main_Slider_admin(admin.ModelAdmin):
    model = Hero_Slider

    list_display = ('title', 'bg_image', 'link')
    search_fields = ('title', 'short_desc')
    list_editable = ['link']

    def image_tag(self, obj):
        return format_html('<img src="{}" style="height:50px; width:50px; border-radius:10px" />'.format(obj.image.url))

class featurs_admin(admin.ModelAdmin):
    model = Hero_Featurs
    list_display = ('title','link', 'color')
    list_editable = ['link','color']

class Tour_Ctgry_admin(admin.ModelAdmin):
    model = Tour_Ctgry
    list_display = ['name']

class Video_TabularInline(admin.TabularInline):
    model = Video

class Place_TabularInline(admin.TabularInline):
    model = Place

class Package_admin(admin.ModelAdmin):
    model = Package
    list_display = ('title', 'category', 'price', 'discount', 'status', 'starting_date', 'duration', 'deadline')
    list_editable = ('category', 'price', 'discount', 'starting_date', 'duration', 'deadline')
    inlines = (Place_TabularInline,Video_TabularInline)

class Service_Admin(admin.ModelAdmin):
    model = Service
    list_display = ('title','link','icon_class','icon_colour','bgPattern_colour')
    list_editable = ['link','icon_colour','bgPattern_colour']


admin.site.register(Hero_Slider,Main_Slider_admin)
admin.site.register(Hero_Featurs,featurs_admin)
admin.site.register(Tour_Ctgry,Tour_Ctgry_admin)
admin.site.register(Package, Package_admin)
admin.site.register(Package_Slider)
admin.site.register(Place)
admin.site.register(Service,Service_Admin)
