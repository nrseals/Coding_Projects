from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.new_user),
    path('login', views.login),
    path('logout', views.logout),
    path('wishes', views.all_wishes),
    path('wishes/new', views.new_wish),
    path('wishes/create', views.create_wish),
    path('wishes/edit/<int:wish_id>', views.edit_wish),
    path('wishes/update/<int:wish_id>', views.update_wish),
    path('wishes/delte/<int:wish_id>', views.delete_wish),
    path('wishes/granted/<int:wish_id>', views.grant_wish),
]