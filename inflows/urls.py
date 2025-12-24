from django.urls import path

from . import views

urlpatterns = [
    path("inflows/list/", views.InflowListView.as_view(), name="inflow_list"),
    path("inflows/create/", views.InflowCreateView.as_view(), name="inflow_create"),
    path(
        "inflow/<int:pk>/detail/",
        views.InflowDetailView.as_view(),
        name="inflow_detail",
    ),
    path(
        "api/v1/inflows/",
        views.InflowCreateListAPIView.as_view(),
        name="inflow_list_create_api",
    ),
    path(
        "api/v1/inflows/<int:pk>/",
        views.InflowRetrieveUpdateDestroyAPIView.as_view(),
        name="inflow_update_destroy_api",
    ),
]
