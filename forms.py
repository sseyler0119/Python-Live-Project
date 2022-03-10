from django.forms import ModelForm
from .models import Recipe
from django import forms


# define RecipeForm
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


# category choices for SearchForm
CATEGORY_OPTIONS = (
        ('Indian High Tea Recipe', 'High Tea Recipes'),
        ('Indian Comfort Food Recipe', 'Comfort Food Recipes'),
        ('Indian Street Food Recipe', 'Indian Street Food Recipes'),
        ('Indian Chicken Recipe', 'Chicken Recipes'),
        ('Beverages Recipe', 'Beverage Recipes'),
        ('Indian Seafood Recipe', 'Seafood Recipes'),
        ('Middle-East Kebab', 'Kebab Recipes'),
        ('Indian One-Pot Recipe', 'One-Pot Recipes'),
        ('Indian Rice Recipe', 'Rice Recipes')
    )


# define SearchForm
class SearchForm(forms.Form):
    category_type = forms.ChoiceField(choices=CATEGORY_OPTIONS)
