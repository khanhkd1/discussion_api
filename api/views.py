from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Count
from api.models import Article, Comment
from api.serializers import (
    ArticleGetSerializer, 
    ArticlePostSerializer, 
    CommentGetSerializer, 
    CommentPostSerializer,
)


class ArticleApiView(APIView, LimitOffsetPagination):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        results = self.paginate_queryset(articles, request, view=self)
        serializer = ArticleGetSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'content': request.data.get('content'), 
            'author': request.data.get('author')
        }
        serializer = ArticlePostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentApiView(APIView, LimitOffsetPagination):
    def get(self, request, *args, **kwargs):
        comments = Comment.objects.filter(root_comment__isnull=True).order_by('updated')
        results = self.paginate_queryset(comments, request, view=self)
        serializer = CommentGetSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'content': request.data.get('content'), 
            'author': request.data.get('author'),
            'article': request.data.get('article'),
            'root_comment': request.data.get('root_comment', None),
        }
        serializer = CommentPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailApiView(APIView):
    def get(self, request, article_id, *args, **kwargs):
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return Response(
                {"res": f"Article with id={article_id} does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ArticleGetSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, article_id, *args, **kwargs):
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return Response(
                {"res": f"Article with id={article_id} does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'content': request.data.get('content'),
        }
        serializer = ArticleGetSerializer(instance=article, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, *args, **kwargs):
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return Response(
                {"res": f"Article with id={article_id} does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        article.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class CommentDetailApiView(APIView):
    def get(self, request, comment_id, *args, **kwargs):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response(
                {"res": f"Comment with id={comment_id} does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CommentGetSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, comment_id, *args, **kwargs):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response(
                {"res": f"Comment with id={comment_id} does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'content': request.data.get('content'),
        }
        serializer = CommentGetSerializer(instance=comment, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id, *args, **kwargs):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response(
                {"res": f"Comment with id={comment_id} does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        comment.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class ArticleTop10ApiView(APIView):
    def get(self, request, *args, **kwargs):
        top10_articles_info = Comment.objects.values('article').annotate(count=Count('article')).order_by('-count', 'article')[:10]
        top10_article_ids = [article['article'] for article in top10_articles_info]
        top10_articles = Article.objects.filter(id__in=top10_article_ids)
        serializer = ArticleGetSerializer(top10_articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
