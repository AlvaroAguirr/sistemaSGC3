from django.urls import path

from . import views

urlpatterns = [
    path("uno", views.index, name="eval2"),
    path("", views.documentos, name="home"),
    path("evalprov", views.evalprov, name="eval")

]
