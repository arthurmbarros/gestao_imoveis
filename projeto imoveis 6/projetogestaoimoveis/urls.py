from django.contrib import admin
from django.urls import path, include
from appgestaoimoveis.views import home, form, create, edit, update, delete, inquilinos, forminquilinos, createinquilinos, deleteinquilinos, editinquilinos, updateinquilinos, imoveis, formimoveis, createimoveis, deleteimoveis, editimoveis, updateimoveis, totalalugueis

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("form/", form, name="form"),
    path("create/", create, name="create"),
    path("edit/<int:pk>/", edit, name="edit"),
    path("update/<int:pk>/", update, name="update"),
    path("delete/<int:pk>/", delete, name="delete"),
    path("inquilinos/", inquilinos, name="inquilinos"),
    path("forminquilinos/", forminquilinos, name="forminquilinos"),
    path("createinquilinos/", createinquilinos, name="createinquilinos"),
    path("deleteinquilinos/<int:pk>/", deleteinquilinos, name="deleteinquilinos"),
    path("editinquilinos/<int:pk>/", editinquilinos, name="editinquilinos"),
    path("updateinquilinos/<int:pk>/", updateinquilinos, name="updateinquilinos"),
    path("imoveis/", imoveis, name="imoveis"),
    path("formimoveis/", formimoveis, name="formimoveis"),
    path("createimoveis/", createimoveis, name="createimoveis"),
    path("deleteimoveis/<int:pk>/", deleteimoveis, name="deleteimoveis"),
    path("editimoveis/<int:pk>/", editimoveis, name="editimoveis"),
    path("updateimoveis/<int:pk>/", updateimoveis, name="updateimoveis"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", totalalugueis, name="totalalugueis"),



]
