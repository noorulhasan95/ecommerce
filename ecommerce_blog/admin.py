from django.contrib import admin

from .models import Post,Category,Subcategory
# Register your models here.

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subname', 'category')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','img_url','category')

admin.site.register(Post,PostAdmin)
# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Subcategory,SubCategoryAdmin)