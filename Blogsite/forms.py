from django import forms
from .models import Post


class Form(forms.ModelForm):
	class Meta:
		model =  Post
		fields = ('title','tag','auther','body')

		widgets = {
				'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
				'tag': forms.TextInput(attrs={'class': 'form-control'}),
				'auther': forms.Select(attrs={'class': 'form-control'}),
				'body': forms.Textarea(attrs={'class': 'form-control'})

		}

class EditForm(forms.ModelForm):
	class Meta:
		model =  Post
		fields = ('title','tag','body')

		widgets = {
				'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
				'tag': forms.TextInput(attrs={'class': 'form-control'}),
				'body': forms.Textarea(attrs={'class': 'form-control'})

		}