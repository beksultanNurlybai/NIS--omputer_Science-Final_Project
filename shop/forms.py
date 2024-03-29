from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comments, Type_of_goods

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email']
		

class CreateCommentsForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('body',)
		widgets = { 'body': forms.Textarea(attrs={
			'cols': None,
			'rows': None,
			'placeholder': 'Оставить комментарий здесь'
		}) }



SORT_CHOICES = [
   ('-updated_at', 'от нового до старого'),
  	('updated_at', 'от старого до нового'),
   ('price', 'сначало дешевые'),
   ('-price', 'сначало дорогие'),
]
FILT_CHOICES = [('0', 'все товары'),] + [(ToG.title, ToG.title) for ToG in Type_of_goods.objects.all()]

class SortFilterForm(forms.Form):
	sort = forms.ChoiceField(choices=SORT_CHOICES, widget=forms.Select(attrs={'onchange': 'submit();'}))
	filt = forms.ChoiceField(choices=FILT_CHOICES, widget=forms.Select(attrs={'onchange': 'submit();'}))



SORT_COMMENTS_CHOICES = [
	('-created_at','сначало новые'),
	('created_at','сначало старые'),
]

class SortCommentsForm(forms.Form):
	sort = forms.ChoiceField(choices=SORT_COMMENTS_CHOICES, widget=forms.Select(attrs={'onchange': 'submit();'}))
