from django import forms 
from .models import Movie

class MovieRatingForm(forms.ModelForm):
	class Meta:
		model = Movie 
		fields = ['rating']
		