from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='desserts_home'),
    path('desserts_add/', views.add_recipe, name='desserts_add'),
    path('desserts_displayDB/', views.display_recipe_items, name='desserts_displayDb'),
    path('<int:pk>/desserts_details/', views.recipe_details, name='desserts_details'),
    path('<int:pk>/desserts_edit/', views.edit_recipe, name='desserts_edit'),
    path('<int:pk>/desserts_delete/', views.delete_recipe, name='desserts_delete'),
    path('desserts_bs/', views.scrape_desserts, name='desserts_bs'),
    # path('desserts_search/', views.recipe_search, name='desserts_search'),
    path('desserts_category_search/', views.category_search, name='desserts_category_search'),
]