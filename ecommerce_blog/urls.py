from django.urls import path
from .import views

app_name = 'ecommerce_blog'

urlpatterns = [
    path("", views.index, name="index"),

    # path("post/<str:slug>", views.detail, name="detail"),

    # path("contact", views.contact_view, name="contact"),
    path("register", views.register, name="register"),
    

    # path("/post/<str:post_id>", views.index2, name="index2"),
]
