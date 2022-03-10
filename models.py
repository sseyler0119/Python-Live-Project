from django.db import models

# define Recipe Type
RECIPE_TYPE = (
    ('Cookies', 'Cookies'),
    ('Cakes', 'Cakes'),
    ('Pies', 'Pies'),
    ('Cupcakes','Cupcakes'),
    ('Bars','Bars'),
    ('Cheesecakes','Cheesecakes'),
    ('Brownies','Brownies'),
    ('Other','Other')
)


# Recipe class model
class Recipe(models.Model):
    category = models.CharField(max_length=20, choices=RECIPE_TYPE, null=False)
    name = models.CharField(max_length=50, default="", blank=True, null=False)
    ingredients = models.TextField(max_length=1000, default="", blank=True, null=False)
    method = models.TextField(max_length=1000, default="", blank=True, null=False)
    servings = models.IntegerField(null=False)

    # returns reference by recipe name
    def __str__(self):
        return self.name

    # objects manager
    Recipes = models.Manager()
