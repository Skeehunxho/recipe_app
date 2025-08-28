from django.urls import path
from .views import RegisterView, CustomAuthToken, RecipeListCreateView, CategoryListView

urlpatterns = [
    path("recipes/", RecipeListCreateView.as_view(), name="recipe-list"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomAuthToken.as_view(), name="login"),
]
