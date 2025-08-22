from django.urls import path
from .views import RecipeListCreateView, CategoryListView

urlpatterns = [
    path("recipes/", RecipeListCreateView.as_view(), name="recipe-list-create"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
]
