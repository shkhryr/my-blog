from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('create/', views.ArticleCreate.as_view(template_name='articles/create.html'), name='create'),
    path('edit/<int:pk>/', views.ArticleEdit.as_view(template_name='articles/edit.html'), name='edit'),
    path('delete/<int:pk>/', views.ArticleDelete.as_view(template_name='articles/delete.html'), name='delete'),
    path('article/<int:pk>/', views.ArticleView.as_view(template_name='articles/article.html'), name='article'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='articles/password_reset.html'),
         name='password_reset'),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(template_name='articles/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='articles/password_reset_confirm.html'),
         name='password_reset_confirm'),

]
