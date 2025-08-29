from django.urls import path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .views import (
    RegisterView, 
    LoginView, 
    RecipeListCreateView, 
    CategoryListCreateView,
    RecipeDetailView,
    CategoryDetailView,   
)

# API root
@api_view(['GET'])
@permission_classes([AllowAny])   
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
    path("recipes/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),  
    path("categories/", CategoryListCreateView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"), 
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"), 
]
