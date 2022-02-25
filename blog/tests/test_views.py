from blog.models import Article, Comment
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestPostViews(TestCase):
    
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
            post_img='https://bblog2.s3.amazonaws.com/post_images/carlos-muza-hpjSkU2UYSU-unsplash.jpg'
        )
        
        self.comment1 = Comment.objects.create(
            post=self.article1,
            author=self.user1,
            comment_content='comment content'
        )
    
    def test_home(self):
        url = reverse('MMblog:home')
        response = self.client.get(url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 
                                'blog/articles.html')
    
    def test_viewing_post(self):
        url = reverse('MMblog:viewing_post', args=[
            self.article1.slug
        ])
        response = self.client.get(url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 
                                'blog/viewing_post.html')
        
    def test_add_comment(self):
        url = reverse('MMblog:viewing_post', args=[
            self.article1.slug
        ])
        response = self.client.post(
            url, {
                'author': 'author1',
                'comment_content': 'This is comment'
            },
            follow=True)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 
                                'blog/viewing_post.html')
        self.assertEquals(Comment.objects.all().count(), 2)
        
    def test_about_me(self):
        url = reverse('MMblog:about_me')
        response = self.client.get(url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 
                                'blog/about_me.html')
        
    def test_projects(self):
        url = reverse('MMblog:projects')
        response = self.client.get(url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 
                                'blog/projects.html')
        
    def test_contact(self):
        url = reverse('MMblog:contact')
        response = self.client.get(url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 
                                'blog/contact.html')
