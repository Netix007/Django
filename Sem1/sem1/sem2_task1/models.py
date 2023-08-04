from django.db import models
from datetime import datetime as dt


class CoinPlay(models.Model):

    throws = []

    side = models.CharField(max_length=10)
    time = models.TimeField(auto_now_add=True)

    @staticmethod
    def get_throws(amount):
        obverse_cnt = 0
        reverse_cnt = 0
        for item in CoinPlay.throws[-amount:]:
            if item[1] == 'obverse':
                obverse_cnt += 1
            else:
                reverse_cnt += 1
        return {'obverse': obverse_cnt, 'reverse': reverse_cnt, }

    @staticmethod
    def add_throws(value):
        sides = ['obverse', 'reverse']
        CoinPlay.throws.append((dt.now(), sides[value]))


class Author(models.Model):

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    biography = models.TextField()
    birthday = models.DateField()

    def get_fullname(self):
        return f'{self.name} {self.surname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    public_date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} {self.published} {self.public_date}'
