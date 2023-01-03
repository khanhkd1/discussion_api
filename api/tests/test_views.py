import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from api.models import Article, Comment
from api.serializers import (
    ArticleGetSerializer, 
    ArticlePostSerializer, 
    CommentGetSerializer, 
    CommentPostSerializer,
)

# python manage.py test api.tests.test_views
# initialize the APIClient app
client = Client()

class GetAllArticlesTest(TestCase):
    """ Test module for GET all articles API """

    def setUp(self):
        article = Article.objects.create(content='Article 1', author='User 1')
        comment = Comment.objects.create(content="Comment 1", author="User 2", article=article)
        Comment.objects.create(content="Reply 1", author="User 1", article=article, root_comment=comment)
        Article.objects.create(content='Article 2', author='User 2')
        Article.objects.create(content='Article 3', author='User 1')
        Article.objects.create(content='Article 4', author='User 3')

    def test_get_all_articles(self):
        # get API response
        response = client.get(reverse('get_post_articles'))
        # get data from db
        articles = Article.objects.all()
        serializer = ArticleGetSerializer(articles, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleArticleTest(TestCase):
    """ Test module for GET single article API """

    def setUp(self):
        self.article_1 = Article.objects.create(content='Article 1', author='User 1')

    def test_get_valid_single_article(self):
        response = client.get(reverse('get_delete_update_article', kwargs={'article_id': self.article_1.pk}))
        article = Article.objects.get(pk=self.article_1.pk)
        serializer = ArticleGetSerializer(article)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_article(self):
        response = client.get(reverse('get_delete_update_article', kwargs={'article_id': 30}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CreateNewArticleTest(TestCase):
    """ Test module for inserting a new article """

    def setUp(self):
        self.valid_payload = {
            'content': 'Article 1',
            'author': 'User 1',
        }
        self.invalid_payload = {
            'content': 'Article 1',
        }

    def test_create_valid_article(self):
        response = client.post(
            reverse('get_post_articles'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_article(self):
        response = client.post(
            reverse('get_post_articles'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleArticleTest(TestCase):
    """ Test module for updating an existing article record """

    def setUp(self):
        self.article_1 = Article.objects.create(content='Article 1', author='User 1')
        self.valid_payload = {
            'content': 'Article 1.1',
        }
        self.invalid_payload = {
            'content': None,
        }

    def test_valid_update_article(self):
        response = client.put(
            reverse('get_delete_update_article', kwargs={'article_id': self.article_1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_article(self):
        response = client.put(
            reverse('get_delete_update_article', kwargs={'article_id': self.article_1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleArticleTest(TestCase):
    """ Test module for deleting an existing article record """

    def setUp(self):
        self.article_1 = Article.objects.create(content='Article 1', author='User 1')

    def test_valid_delete_article(self):
        response = client.delete(
            reverse('get_delete_update_article', kwargs={'article_id': self.article_1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete_article(self):
        response = client.delete(
            reverse('get_delete_update_article', kwargs={'article_id': 30}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
