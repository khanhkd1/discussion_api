from django.db import models
from django.utils import timezone
from django.forms.models import model_to_dict


class Article(models.Model):
    content = models.TextField(blank=True, null=False)
    author = models.CharField(max_length=50, null=False)
    created = models.DateTimeField(default=timezone.now, null=False, editable=False)
    updated = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return f"{self.updated}, {self.author}: {self.content}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Article, self).save(*args, **kwargs)
    
    def all_comments(self):
        comments_queryset = Comment.objects.filter(root_comment__isnull=True, article=self.id)
        comments = []
        for comment_queryset in comments_queryset:
            replies = comment_queryset.all_replies()
            comment = model_to_dict(comment_queryset)
            comment['all_replies'] = replies
            comments.append(comment)
        return comments

    class Meta:
        db_table = 'article'
        indexes = [
            models.Index(fields=['id']),
        ]


class Comment(models.Model):
    content = models.TextField(blank=True, null=False)
    author = models.CharField(max_length=50, null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False, related_name="comment", db_column='article')
    root_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name="reply", db_column='root_comment')
    created = models.DateTimeField(default=timezone.now, null=False, editable=False)
    updated = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return f"{self.updated}, {self.author}: {self.content}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Comment, self).save(*args, **kwargs)
    
    def all_replies(self):
        return Comment.objects.filter(root_comment=self.id).values()

    class Meta:
        db_table = 'comment'
        indexes = [
            models.Index(fields=['id', 'article']),
        ]
