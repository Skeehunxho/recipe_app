from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Recipe, Category


# -------- API ROOT TEST --------
class ApiRootTests(APITestCase):
    def test_api_root_accessible_without_auth(self):
        url = reverse("api-root")
        response = self.client.get(url)  # No auth token provided
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_keys = {"recipes", "categories", "register", "login"}
        self.assertEqual(set(response.data.keys()), expected_keys)


# -------- AUTH TESTS 
class AuthTests(APITestCase):
    def test_user_registration_and_token_returned(self):
        url = reverse("register")
        data = {"username": "testuser", "password": "testpass123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("token", response.data)
        self.assertIn("username", response.data)

    def test_user_login_returns_token(self):
        # Create user
        user = User.objects.create_user(username="testuser", password="testpass123")

        url = reverse("login")
        data = {"username": "testuser", "password": "testpass123"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
        self.assertEqual(response.data["username"], user.username)


# -------- RECIPE TESTS 
class RecipeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client.login(username="testuser", password="testpass123")
        self.category = Category.objects.create(name="Dessert")  # Create a category to use

    def test_create_recipe_authenticated(self):
        url = reverse("recipe-list")
        data = {
            "title": "Test Recipe",
            "description": "Yummy food",
            "ingredients": "Flour, Sugar, Eggs",
            "instructions": "Mix and bake",
            "preparation_time": 10,
            "cooking_time": 20,
            "servings": 2,
            "category": self.category.id,  # required foreign key
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)
        recipe = Recipe.objects.get()
        self.assertEqual(recipe.title, "Test Recipe")
        self.assertEqual(recipe.created_by, self.user)
        self.assertEqual(recipe.category, self.category)

    def test_list_recipes(self):
        Recipe.objects.create(
            title="Recipe 1",
            description="Desc",
            ingredients="Flour, Sugar",
            instructions="Mix and cook",
            created_by=self.user,
            category=self.category,
        )
        url = reverse("recipe-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


# -------- CATEGORY TESTS 
class CategoryTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client.login(username="testuser", password="testpass123")

    def test_create_category_authenticated(self):
        url = reverse("category-list")
        data = {"name": "Breakfast"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, "Breakfast")

    def test_list_categories(self):
        Category.objects.create(name="Dinner")
        url = reverse("category-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
