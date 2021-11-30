from django.urls import path, include
from . import views

urlpatterns = [
    path("create", views.populate_table, name="populate"),
    path("get_entity", views.get_medicine, name="entity"),
]