from django import forms

from movieapp.models import Movie


class Movie_Form(forms.ModelForm):
        class Meta:
                    model = Movie
                    fields = ['name','desc','year','img']