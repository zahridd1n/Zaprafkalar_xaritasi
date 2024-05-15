from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view()),
    path('detail/<int:id>/', views.ZaprafkaDetailView.as_view()),

    path('register/', views.register),
    path('login/', views.log_in),
    path('logout/', views.log_out),

    path('category/create/', views.CategoryCreate.as_view()),
    path('category/edit/<int:pk>/', views.CategoryEdit.as_view()),
    path('zaprafka/create/', views.zaprafka_create),
    path('zaprafka/edit/<int:id>/', views.ZaprafkaEdit.as_view()),

]
