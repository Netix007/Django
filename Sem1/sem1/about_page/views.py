from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

html = """
    <h1>Обо мне</h1>
    <p>Это страница с информацией обо мне. Тут будет добавлено все самое интересное.</p>
"""


def about_page(request):
    logger.info(f'About page accessed.')
    return HttpResponse(html)
