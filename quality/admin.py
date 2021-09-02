from django.contrib import admin
from .models import Images,Category,Location

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('category','location')

admin.site.register(Images,ImageAdmin)
admin.site.register(Category)
admin.site.register(Location)