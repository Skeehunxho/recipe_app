from django.urls import path
from .views import RecipeListCreateView, CategoryListView

urlpatterns = [
    path("recipes/", RecipeListCreateView.as_view(), name="recipe-list-create"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
]
from .views import register
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', obtain_auth_token, name='login'),
]
