from django.test import TestCase
from api.models import Article, Comment


# python manage.py test api.tests.test_models.ArticleCommentTestCase.content_and_foreign_key
class ArticleCommentTestCase(TestCase):
    def setUp(self):
        article = Article.objects.create(content="Test article", author="KhanhKD1 article")
        Comment.objects.create(content="Test comment", author="KhanhKD1 comment", article=article)

    def content_and_foreign_key(self):
        article = Article.objects.get(content="Test article")
        comment = Comment.objects.get(content="Test comment")
        
        self.assertEqual(f'{article.content} - {article.author}', 'Test article - KhanhKD1 article')
        self.assertEqual(f'{comment.content} - {comment.author}', 'Test comment - KhanhKD1 comment')
        self.assertEqual(comment.article.id, article.id)
