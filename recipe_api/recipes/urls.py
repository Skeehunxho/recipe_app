from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .views import RegisterView, CustomAuthToken, RecipeListCreateView, CategoryListView


# API root
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'recipes': reverse('recipe-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),
        'register': reverse('register', request=request, format=format),
        'login': reverse('login', request=request, format=format),
    })


urlpatterns = [
    path("", api_root, name="api-root"),  
    path("recipes/", RecipeListCreateView.as_view(), name="recipe-list"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomAuthToken.as_view(), name="login"),
]
