from blog.models import Article, Comment
from django.contrib.auth.models import User
from django.test import TestCase


class ArticleCommentTest(TestCase):
    
    def setUp(self):
        self.user1 = User.objects.create(
            username='my_nickname',
            email='name@invalid.com',
        )
        self.user1.set_password("my_paSW1")
        self.user1.save()

        self.article1 = Article.objects.create(
            author=self.user1,
            title='This is my first article',
            slug='this-is-my-first-article',
            post_pre_content='123',
        )
        
        self.comment1 = Comment.objects.create(
            post=self.article1,
            author=self.user1,
            comment_content='comment content'
        )
        
    def test_article_str(self):
        self.assertEqual(self.article1.__str__(), 
                         self.article1.title)
        
    def test_comment_str(self):
        self.assertEqual(self.comment1.__str__(), 
                         self.comment1.comment_content)
