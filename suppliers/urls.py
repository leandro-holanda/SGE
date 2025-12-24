from django.urls import path

from . import views

urlpatterns = [
    path("suppliers/list/", views.SupplierListView.as_view(), name="supplier_list"),
    path(
        "suppliers/create/", views.SupplierCreateView.as_view(), name="supplier_create"
    ),
    path(
        "supplier/<int:pk>/detail/",
        views.SupplierDetailView.as_view(),
        name="supplier_detail",
    ),
    path(
        "supplier/<int:pk>/update/",
        views.SupplierUpdateView.as_view(),
        name="supplier_update",
    ),
    path(
        "supplier/<int:pk>/delete/",
        views.SupplierDeleteView.as_view(),
        name="supplier_delete",
    ),
    path(
        "api/v1/suppliers/",
        views.SupplierCreateListAPIView.as_view(),
        name="supplier_create_list_api",
    ),
    path(
        "api/v1/suppliers/<int:pk>/",
        views.SupplierRetrieveUpdateDestroyAPIView.as_view(),
        name="supplier_update_destroy_api",
    ),
]
