from django.contrib import admin

from .models import *


class CommentsAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'body', 'good', 'created_at', 'is_published')
	list_display_links = ('id', 'good', 'user')
	search_fields = ('user', 'body', 'good')

admin.site.register(Comments, CommentsAdmin)

class GoodsAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'price', 'ingredients', 'created_at', 'updated_at', 'type_of_goods', 'is_published')
	list_display_links = ('id', 'title', 'type_of_goods')
	search_fields = ('title', 'ingredients')

admin.site.register(Goods, GoodsAdmin)



class Type_of_goodsAdmin(admin.ModelAdmin):
	list_display = ('id', 'title')
	list_display_links = ('id', 'title')
	search_fields = ('title',)

admin.site.register(Type_of_goods, Type_of_goodsAdmin)