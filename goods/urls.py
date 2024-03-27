from django.forms import inlineformset_factory
from django.urls import include, path
from . import views

app_name = "goods"

urlpatterns = [
    path("<slug:category_slug>/", views.catalog, name="index"),
    path("<slug:category_slug>/<int:page>/", views.catalog, name="index"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]
