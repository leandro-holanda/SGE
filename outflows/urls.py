from django.urls import path

from . import views

urlpatterns = [
    path("outflows/list/", views.OutflowListView.as_view(), name="outflow_list"),
    path("outflows/create/", views.OutflowCreateView.as_view(), name="outflow_create"),
    path(
        "outflow/<int:pk>/detail/",
        views.OutflowDetailView.as_view(),
        name="outflow_detail",
    ),
    path(
        "api/v1/outflows/",
        views.OutflowCreateListAPIView.as_view(),
        name="outflow_list_create_api",
    ),
    path(
        "api/v1/outflows/",
        views.OutflowRetrieveUpdateDestroyAPIView.as_view(),
        name="outflow_update_destroy_api",
    ),
]
