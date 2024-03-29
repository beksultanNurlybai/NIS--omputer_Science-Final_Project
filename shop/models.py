from django.db import models
from django.contrib.auth.models import User

class Comments(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name='Пользователь')
	good = models.ForeignKey('Goods', on_delete=models.PROTECT, null=True, related_name='comments', verbose_name='Товар')
	body = models.TextField(verbose_name='Комментарий')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
	is_published = models.BooleanField(default=True, verbose_name='Публиковать')

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
		ordering = ['-created_at']


class Goods(models.Model):
	title = models.CharField(max_length=100, verbose_name='Имя товара')
	price = models.IntegerField(verbose_name='Цена')
	ingredients = models.CharField(max_length=300, verbose_name='Ингедиенты', null=True, blank=True)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменении')
	is_published = models.BooleanField(default=True, verbose_name='Публиковать')
	type_of_goods = models.ForeignKey('Type_of_goods', on_delete=models.PROTECT, null=True, verbose_name='Тип товара')

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
		ordering = ['-created_at']
		
	def __str__(self):
		return self.title


class Type_of_goods(models.Model):
	title = models.CharField(max_length=100, db_index=True, verbose_name='Название типа товара')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Тип'
		verbose_name_plural = 'Типы'
		ordering = ['title']