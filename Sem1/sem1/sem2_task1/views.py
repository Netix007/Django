from django.shortcuts import render, get_object_or_404
from sem2_task1.models import Author, Article
from sem2_task1.forms import AuthorForms, ArticleForms
from django import forms
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


def add_author(request):
    if request.method == 'POST':
        form = AuthorForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')
            email = form.cleaned_data.get('email')
            biography = form.cleaned_data.get('biography')
            birthday = form.cleaned_data.get('birthday')

            logger.info(f'New author: {name} {surname} {email} {biography} {birthday}')

    else:
        form = AuthorForms()
    return render(request=request, template_name='sem2_task1/author_forms.html', context={'form': form})


def add_article(request):
    if request.method == 'POST':
        form = ArticleForms(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            author = form.cleaned_data.get('author')
            category = form.cleaned_data.get('category')

            article = Article(
                title=title,
                content=content,
                author=author,
                category=category,
            )
            article.save()
            logger.info(f'New article: {article}')

    else:
        form = ArticleForms()
    return render(request=request, template_name='sem2_task1/article_forms.html', context={'form': form})
