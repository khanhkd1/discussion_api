from django.urls import path
from api.views import (
    ArticleApiView,
    CommentApiView,
    ArticleDetailApiView,
    CommentDetailApiView,
    ArticleTop10ApiView,
)

urlpatterns = [
    path('article', ArticleApiView.as_view(), name='get_post_articles'),
    path('article/<int:article_id>/', ArticleDetailApiView.as_view(), name='get_delete_update_article'),
    path('comment', CommentApiView.as_view()),
    path('comment/<int:comment_id>/', CommentDetailApiView.as_view()),
    path('article/top10/', ArticleTop10ApiView.as_view()),
]
