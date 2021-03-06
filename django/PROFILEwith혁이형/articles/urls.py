from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/comments/', views.create_comment, name='create_comment'),
    path('<int:article_pk>/comments/<comment_pk>/delete/', views.delete_comment, name='delete_comment'),
    # 좋아요 누르는 게시물이 몇번째거인지 알아야하니까 article_pk 필요함.
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
