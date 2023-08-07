from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import logging

logger = logging.getLogger(__name__)

html = """
    <h1>Главная страница</h1>
    <p>Это главная страница. Тут надо добавить какое-то описание.</p>
"""


def main_page(request):
    logger.info(f'Main page accessed.')
    return HttpResponse(html)


def hello(request: HttpRequest):
    logger.info("hello running...")
    return HttpResponse("<h1>Hello, world!</h1>")


def index_page(request: HttpRequest):

    context = {'title': 'Главная', 'content': 'Главная страница'}

    logger.info(
        f"Access to main page from {request.META.get('REMOTE_ADDR')}, user agent: {request.META.get('HTTP_USER_AGENT')}"
    )
    return render(request, template_name='main_page/index.html', context=context)


def about_page(request: HttpRequest):
    context = {'title': 'Обо мне', 'content': 'Обо мне'}

    logger.info(
        f"Access to main page from {request.META.get('REMOTE_ADDR')}, user agent: {request.META.get('HTTP_USER_AGENT')}"
    )
    return render(request, template_name='main_page/about.html', context=context)
