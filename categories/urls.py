from django.urls import path

from . import views

urlpatterns = [
    path("categories/list/", views.CategoryListView.as_view(), name="category_list"),
    path(
        "categories/create/", views.CategoryCreateView.as_view(), name="category_create"
    ),
    path(
        "category/<int:pk>/detail/",
        views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
    path(
        "category/<int:pk>/update/",
        views.CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "category/<int:pk>/delete/",
        views.CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path(
        "api/v1/categories/",
        views.CategoryCreateListAPIView.as_view(),
        name="category_list_create_api_view",
    ),
    path(
        "api/v1/categories/<int:pk>/",
        views.CategoryRetrieveUpdateDestroyAPIView.as_view(),
        name="category_list_create_api_view",
    ),
]
