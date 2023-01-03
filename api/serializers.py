from rest_framework import serializers
from api.models import Article, Comment


class CommentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "content", "article", "root_comment", "all_replies"]


class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "content", "article", "root_comment"]


class ArticleGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "author", "content", "created", "updated", "all_comments"]


class ArticlePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "author", "content"]
