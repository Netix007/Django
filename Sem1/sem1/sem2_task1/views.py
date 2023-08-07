from django.shortcuts import render, get_object_or_404
from sem2_task1.models import Author, Article
from django.utils.safestring import mark_safe
import logging

logger = logging.getLogger(__name__)


def get_article_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    articles = Article.objects.filter(author=author)

    context = {
        'title': 'Статьи автора',
        'autor': author,
        'articles': articles
    }
    return render(request, template_name='sem2_task1/articles.html', context=context)


def get_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    context = {
        'title': article.title,
        'article': article
    }
    return render(request, template_name='sem2_task1/article.html', context=context)
