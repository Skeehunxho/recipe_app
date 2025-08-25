from django.urls import path
from .views import register, CustomAuthToken, RecipeListCreateView, CategoryListView

urlpatterns = [
    path("recipes/", RecipeListCreateView.as_view(), name="recipe-list"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("register/", register, name="register"),
    path("login/", CustomAuthToken.as_view(), name="login"),
]
